from django.db import models


# Create your models here.
class RoomMsg(models.Model):

    room_num = models.CharField(max_length=10, primary_key=True, unique=True, help_text="房间号")
    room_type = models.CharField(max_length=20,  help_text="房间类型")
    room_appliance = models.CharField(max_length=100, help_text="房间设备")
    room_window = models.CharField(max_length=10, help_text="是否有窗")
    room_max_num = models.CharField(max_length=10, help_text="推荐最大居住人数")
    islive = models.CharField(max_length=100, help_text="是否有人居住")
    peo_num = models.CharField(max_length=2, help_text="入住人数", default=0)
    house_tel = models.CharField(max_length=10, help_text="客房电话", default=101)

    class Meta:
        db_table = "room_msg"




