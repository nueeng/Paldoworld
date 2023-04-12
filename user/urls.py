from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.userlist_view, name='userlist'),
    path('user/follow/<int:id>', views.follow_view,name='follow'),

]
