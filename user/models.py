from django.db import models


# Create your models here.
class User_password(models.Model):
    user = models.CharField(max_length=20, primary_key=True, unique=True, help_text="账户")
    password = models.CharField(max_length=200, unique=True, help_text="密码")
    email = models.CharField(max_length=200, help_text="邮箱", default="xxyy@xx.com")

    class Meta:
        db_table = "user"