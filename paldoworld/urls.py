from django.contrib import admin
from django.urls import path, include

from django.conf import settings # 이미지 업로드 위해 static파일을 media 디렉터리에서 가져오겠다.
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
    path('',include('tweet.urls')),
    path('',include('guestbook.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
