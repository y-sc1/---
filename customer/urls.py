from django.urls import path
from . import views

urlpatterns = [

    path("<int:room_num>", views.getin_room),
    path("message", views.message),
    path("index", views.index),
    path("check_out", views.check_out),
    path("customer_record", views.msg_record)
]