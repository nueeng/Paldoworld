from django.db import models
from user.models import UserModel

class GuestbookModel(models.Model):
    class Meta:
        db_table = "guestbook"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="guestbook_author")
    author_nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE, max_length=30, related_name="guestbook_author_nickname")
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
