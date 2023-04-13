from django.contrib import admin #장고에서 admin을사용하겠다~!
from .models import UserModel #우리가 현재위치에(.)생성한 .models에있는 usermodel을사용한다.

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
