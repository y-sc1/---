# Generated by Django 3.0.3 on 2020-05-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMsg',
            fields=[
                ('room_num', models.CharField(help_text='房间号', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('room_type', models.CharField(help_text='房间类型', max_length=20)),
                ('room_appliance', models.CharField(help_text='房间设备', max_length=100)),
                ('room_window', models.CharField(help_text='是否有窗', max_length=10)),
                ('room_max_num', models.CharField(help_text='推荐最大居住人数', max_length=10)),
                ('islive', models.CharField(help_text='是否有人居住', max_length=100)),
            ],
        ),
    ]