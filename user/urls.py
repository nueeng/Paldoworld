from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile_edit/', views.profile_edit_view, name='profile_edit'),
    path('follow/', views.userlist_view, name='userlist'),
    path('follow/<int:id>', views.follow_view,name='follow'),

]
