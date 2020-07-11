"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
from django.conf.urls import url
from django.urls.conf import include

urlpatterns = [
    # path('/', admin.site.urls),
    url("^query/", include("roommsg.urls")),
    path("index", view.index),
    url("^getin/", include("customer.urls")),
    url("^customer_msg/", include("customer.urls")),
    url("^roommsg/", include("roommsg.urls")),
    path("account", view.account),
    path("login", view.login),
    path("record", view.record),
    path("room", view.room),
    path("password", view.psw),
    url("^user/", include("user.urls")),
    path("forget_pwd", view.forget_pwd),
    url("^$", view.login),
]
