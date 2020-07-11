from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from roommsg.models import RoomMsg as rm
import json
import hashlib
from . import decorators


@decorators.auto_session
def psw(request):
    return render(request, "password.html")


# 主页
@decorators.auto_session
def index(request):
    return render(request, "index.html")


# 跳转到登记页面
@decorators.auto_session
def getIn(request):
    return render(request, "GetIn.html")


# 数据
@decorators.auto_session
def account(request):
    return render(request, "AccountCenter.html")


@decorators.auto_session
def record(request):
    return render(request, "RoomRecord.html")


# 房间信息
@decorators.auto_session
def room(request):
    # 首页搜索跳转，带参数
    if request.POST.dict() != {}:
        record_text = request.POST.dict()["record_text"]

        if record_text == "空房":
            room_msg = rm.objects.filter(islive="否")
        elif record_text == "有客房间":
            room_msg = rm.objects.filter(islive="是")
        elif record_text in ["大床房", "双人间", "三人间", "家庭房"]:
            room_msg = rm.objects.filter(room_type=record_text)
        else:
            try:
                room_num = int(record_text)
            except:
                return redirect("/index")
            else:
                room_msg = rm.objects.filter(room_num=room_num)
    # 直接访问，不带参数
    else:
        room_msg = rm.objects.all()
    # 做汉字数字与阿拉伯数字的映射
    number_dict = {
                    "一楼": "10",
                    "二楼": "20",
                    "三楼": "30",
                    "四楼": "40",
                    "五楼": "50",
                    "六楼": "60",
                    "七楼": "70",
                    "八楼": "80",
                     }

    return render(request, "room.html", {"room_msg": room_msg, "number_dict": number_dict})


# 登录
def login(request):
    return render(request, "login.html")


def forget_pwd(request):
    return render(request, "forget_password.html")
