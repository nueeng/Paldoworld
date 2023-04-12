from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'), # 여기가 사이트 진입 url path 같습니다
    path('main/', views.main, name='main'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete-tweet'),
    path('tweet/edit/<int:id>', views.edit_tweet, name='edit-tweet'),
    path('tweet/update/<int:id>', views.update_tweet, name='update-tweet'),
    path('tweet/<int:id>', views.detail_tweet, name='detail-tweet'),
    path('tweet/comment/<int:id>', views.write_comment, name='write-comment'),
    path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
    
]
