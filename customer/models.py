from django.db import models

# Create your models here.


class Customer(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,  help_text="姓名")
    __choice_type = [("m", "男"), ("f", "女")]
    sex = models.CharField(max_length=1, choices=__choice_type, help_text="性别")
    id_card = models.CharField(max_length=100, help_text="身份证号")
    live_room = models.CharField(max_length=10, help_text="入住房间")
    deposit = models.CharField(max_length=10, help_text="押金,单位元")
    live_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "customer"


class Check_out(models.Model):

    id = models.IntegerField(auto_created=True),
    name = models.CharField(max_length=20, help_text="姓名")
    sex = models.CharField(max_length=1, help_text="性别")
    id_card = models.CharField(max_length=100, help_text="身份证号")
    live_room = models.CharField(max_length=10, help_text="入住房间")
    deposit = models.CharField(max_length=50, help_text="押金是否退还")
    damage_record = models.CharField(max_length=100, blank=True, help_text="损坏记录", default="无")
    consume_record = models.CharField(max_length=100, blank=True, help_text="消费记录", default=0)
    live_time = models.DateTimeField(max_length=100, help_text="入住时间")
    check_out_time = models.DateTimeField(auto_now=True, help_text="退房时间")

    class Meta:
        db_table = "check_out_record"

