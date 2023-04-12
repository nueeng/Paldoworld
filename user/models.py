#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    nickname = models.CharField(max_length=256, default='') # 상태정보
    speech = models.CharField(max_length=256, default='') # 상태정보
    site_address = models.CharField(max_length=256, default='') # 상태정보
    tmi = models.CharField(max_length=256, default='') # 상태정보
