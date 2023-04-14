#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings # follow model 추가 


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    nickname = models.CharField(max_length=256, default='') # 상태정보
    speech = models.CharField(max_length=256, default='') # 상태정보
    site_address = models.CharField(max_length=256, default='') # 상태정보
    tmi = models.CharField(max_length=256, default='') # 상태정보
    birthday = models.DateField(null=True, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower') # follow model 추가 / follow 기능 쓰려면 migrate 다시 해야함!
    image = models.ImageField(upload_to="", null=True, blank=True) # 여기서 upload_to="", 는 MEDIA_ROOT를 의미합니다.
