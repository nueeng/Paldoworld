from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from user.models import UserModel


# Create your models here.
class GuestbookModel(models.Model):
    class Meta:
        db_table = "guestbook"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
