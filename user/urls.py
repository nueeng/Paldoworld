from django.urls import path
from . import views
<<<<<<< HEAD

=======
>>>>>>> 605e662dbf1d04c4f35ea3f53ee4d49d1c2291d4
urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
]