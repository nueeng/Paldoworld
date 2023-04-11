from django.db import models
from user.models import UserModel


# Create your models here.
class GuestbookModel(models.Model):
    class Meta:
        db_table = "guestbook"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
