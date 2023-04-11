#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

<<<<<<< HEAD
    nickname = models.CharField(max_length=256, default='') # 상태정보
    speech = models.CharField(max_length=256, default='') # 상태정보
    site_address = models.CharField(max_length=256, default='') # 상태정보
    tmi = models.CharField(max_length=256, default='') # 상태정보
=======
    nickname = models.CharField(max_length=256, default='너는 닉네임이 뭐야?') # 상태정보
    speech = models.CharField(max_length=256, default='하고싶은말 있으면 같이적어줘') # 상태정보
    site_address = models.CharField(max_length=256, default='git, blog주소작성해줘') # 상태정보
    tmi = models.CharField(max_length=256, default='너의 tmi를 작성해줘') # 상태정보
>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
