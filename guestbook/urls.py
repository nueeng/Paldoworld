from django.urls import path
from . import views

urlpatterns = [
    path('guestbook/', views.guestbook, name='guestbook'),
    path('edit/<int:id>', views.edit_guestbook, name='edit'),
    path('delete/<int:id>', views.delete_guestbook, name='delete'),
    path('<str:username>/', views.view_guestbook, name='view'),
]
#path('<str:username>/', views.view_guestbook, name='view'),
# = OO님의 방명록 에서 OO을 출력하는데 사용
