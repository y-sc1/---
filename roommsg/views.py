from django.shortcuts import render
from .models import RoomMsg as rm
from customer.models import Customer as cu
# from .models import Check_out as co
from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.


# 展示房间信息
def room_msg(request, room_num):
    room_msg = rm.objects.get(room_num=room_num)
    data = {# 房间号
            "room_num": room_num,
            # 房间类型
            "room_type": room_msg.room_type,
            # 房间设备
            "room_appliance": room_msg.room_appliance,
            # 是否有窗
            "room_window": room_msg.room_window,
            # 房间人数
            "room_max_num": room_msg.room_max_num,
            # 是否有住户
            "islive": room_msg.islive,
            #  客房电话
            "house_tel": room_msg.house_tel
    }
    if room_msg.islive == "是":
        customer = cu.objects.filter(live_room=room_num)
        live_people = ""
        for i in range(len(customer)):
            if customer[i].sex == "男":
                live_people += customer[i].name + "先生"+"  "
            else:
                live_people += customer[i].name + "女士"+"  "

        data1 = {
            # 押金
            "deposit": customer[0].deposit,
            # 居住人数
            "peo_num": room_msg.peo_num,
            #入住时间
            "live_time": str(customer[0].live_time).split(".")[0],
            # 住户姓名
            "live_people": live_people
        }

        data.update(data1)
    else:
        pass
    data = json.dumps(data)
    return HttpResponse(data)

