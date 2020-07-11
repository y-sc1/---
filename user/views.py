from django.shortcuts import render
from .models import User_password as userp
from django.shortcuts import redirect
import hashlib
import json
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.core.mail import EmailMessage
from MyDjango import decorators
# Create your views here.


# 登录验证
def testing(request):
    name = request.POST.get("username")
    password = request.POST.get("password")
    # 对密码做md5加密
    md = hashlib.md5()
    md.update(password.encode())
    password = md.hexdigest()
    # 查询用户密码是否正确
    user = userp.objects.filter(user=name, password=password)
    if user.count() == 0:
        status = "400"
    else:
        status = "200"
        # 将用户信息添加到session中
        md.update((name + password).encode())
        user = md.hexdigest()
        request.session["user"] = user
    data = json.dumps({"status": status})
    return HttpResponse(data)


sql_account = ""


# 修改密码时检查用户信息
def check_user(request):
    global sql_account
    data = request.POST.dict()
    if data["status"] == "acc":
        sql_account = data["account"]
        try:
            userp.objects.get(user=sql_account)
        except:
            msg = {"status": "500", "msg": "账户不正确"}
        else:
            msg = {"status": "200", "msg": "账户正确"}
    else:
        md = hashlib.md5()
        md.update(data["account"].encode())
        password = md.hexdigest()
        if userp.objects.filter(password=password, user=sql_account).count() == 0:
            msg = {"status": "500", "msg": "密码错误或密码账户不匹配"}
        else:
            msg = {"status": "200", "msg": "密码匹配成功"}

    msg = json.dumps(msg)
    return HttpResponse(msg)


# 修改密码
@decorators.auto_session
def change_pwd(request):
    data = request.POST.dict()
    md = hashlib.md5()
    md.update(data["new_pwd"].encode())
    password = md.hexdigest()
    userp.objects.filter(user=data["acc"]).update(password=password)
    request.session.flush()
    return HttpResponseRedirect("http://127.0.0.1:8000")


# 找回密码
def forget_pwd(request):
    account_dict = request.POST.dict()
    email = account_dict["email"]
    user = account_dict["account"]
    change_user = userp.objects.filter(user=user)
    if change_user.count() == 0:
        data = {"status": 500, "msg": "您的账户不正确"}
    else:
        if change_user[0].email == email:
            # 生成6位新密码
            key1 = [str(a) for a in range(10)]
            key2 = [chr(a) for a in range(65, 92)]
            key3 = [chr(a) for a in range(97, 123)]
            keys = key1 + key2 + key3
            key = random.choices(keys, k=6)
            key_s = ""
            for k in key:
                key_s += k
            # md5加密
            md = hashlib.md5()
            md.update(key_s.encode())
            password = md.hexdigest()
            # 存入数据库
            userp.objects.filter(user=user).update(password=password)

            # 发送邮件
            body = "您的新密码是："+key_s+"，请及时修改您的密码"
            message = EmailMessage(subject="密码找回", body=body, to=(email,))
            message.send()

            data = {"status": 200, "msg": "新密码已发送至您的邮箱，请注意查收"}
        else:
            data = {"status": 500, "msg": "账户与邮箱不匹配"}

    data = json.dumps(data)
    return HttpResponse(data)


def logout(request):
    request.session.flush()

    return redirect(to="/")