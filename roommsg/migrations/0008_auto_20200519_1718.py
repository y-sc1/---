# Generated by Django 3.0.3 on 2020-05-19 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roommsg', '0007_delete_user_password'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='roommsg',
            table='room_msg',
        ),
    ]