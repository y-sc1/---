# Generated by Django 3.0.3 on 2020-05-09 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommsg', '0002_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommsg',
            name='peo_num',
            field=models.CharField(default=0, help_text='入住人数', max_length=2),
        ),
    ]