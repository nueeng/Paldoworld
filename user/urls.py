from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
]
