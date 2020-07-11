from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer as cu
from .models import Check_out as co
from MyDjango import decorators
from roommsg.models import RoomMsg as rm
import json

# Create your views here.


def getin_room(request, room_num):

    return render(request, "getin.html")


# 确认入住后重定向到首页
def index(request):
    return HttpResponseRedirect(redirect_to="http://127.0.0.1:8000/index")


# 登记入住
def message(request):

    # 获取前台字典数据
    data = request.POST.dict()
    # 将值转换为列表
    data_values = list(data.values())

    # 获取入住房间号
    room_num = data_values[-1]
    room_msg = rm.objects.filter(room_num=room_num)
    if room_msg[0].islive == "否":
        data_values.pop(-1)
        # 获取入住人数
        peo_num = data_values[4]
        data_values.pop(4)
        # 列表推导式获取客户列表
        data_values = [data_values[i:i+4] for i in range(0, len(data_values), 4)]
        # for i in range(0, len(data_values), 4):
        #     print(data_values[i:i+4])
        try:
            for i in range(len(data_values)):
                if data_values[i][0] != "" and data_values[i][2] != "" and data_values[i][3] != "":
                    cu.objects.create(name=data_values[i][0], sex=data_values[i][1], id_card=data_values[i][2],
                                      deposit=data_values[i][3], live_room=room_num)
                else:
                    raise ValueError
            rm.objects.filter(room_num=room_num).update(peo_num=peo_num, islive="是")
        except:
            msg = {"msg": "录入失败，请重试", "status": 500}
        else:
            msg = {"msg": "录入成功", "status": 200}
    else:
        msg = {"msg": "该房间已有住户", "status": 200}
    msg = json.dumps(msg)
    return HttpResponse(msg)


# 退房
def check_out(request):
    data = request.POST.dict()
    room_num = data["room_num"]

    # 查询房间住户信息
    customer_list = cu.objects.filter(live_room=data["room_num"])
    # print(customer_list[0])
    for i in customer_list:
        # 姓名
        name = i.name
        # 性别
        sex = i.sex
        # 身份证号
        id_card = i.id_card
        # 押金
        deposit = i.deposit + ","+data["deposit"]
        # 入住时间
        live_time = i.live_time
        # 将数据存入退房记录表
        co.objects.create(name=name, sex=sex, id_card=id_card, live_room=room_num, deposit=deposit,
                          damage_record=data["damage_text"], consume_record=data["consume"], live_time=live_time)
    # 将住户表中的数据删除
    cu.objects.filter(live_room=room_num).delete()
    # 将房间信息改成空房
    rm.objects.filter(room_num=room_num).update(islive="否", peo_num=0)
    return redirect("/room")


# 查询住房记录
def msg_record(request):
    record_text = request.POST.dict()["record_text"]
    record_type = request.POST.dict()["record_type"]
    # 判断查询方式
    if record_type == "name":
        # 以姓名为关键字查询
        customer_1 = co.objects.filter(name__contains=record_text)
        customer_2 = cu.objects.filter(name__contains=record_text)
    elif record_type == "sex":
        # 以性别为关键字查询
        customer_1 = co.objects.filter(sex=record_text)
        customer_2 = cu.objects.filter(sex__contains=record_text)
    elif record_type == "live_time":
        # 已入住时间为关键字查询
        customer_1 = co.objects.filter(live_time__contains=record_text)
        customer_2 = cu.objects.filter(live_time__contains=record_text)
    elif record_type == "room_num":
        # 以房间号为关键字查询
        customer_1 = co.objects.filter(live_room__contains=record_text)
        customer_2 = cu.objects.filter(live_room__contains=record_text)
    data = []
    message = {}
    if customer_1.count() != 0 or customer_2.count() != 0:
        # 将查询到的数据放入list中
        for i in range(len(customer_1)):
            message["name"] = customer_1[i].name
            message["sex"] = customer_1[i].sex
            message["id_card"] = customer_1[i].id_card
            message["live_time"] = customer_1[i].live_time.strftime("%Y-%m-%d %H-%M-%S")
            message["check_out_time"] = customer_1[i].check_out_time.strftime("%Y-%m-%d %H-%M-%S")
            message["room_num"] = customer_1[i].live_room
            data.append(message)
            message = {}
        data.append({"status": 200})
    else:
        data = []
        data.append({"msg": "未查询到信息", "status": 500})

    data = json.dumps(data)

    return HttpResponse(data)