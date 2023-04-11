from django.urls import path
from . import views

urlpatterns = [
    path('guestbook/', views.guestbook, name='guestbook'),
    path('guestbook/edit/<int:id>', views.edit_guestbook, name='edit-guestbook'),
    path('guestbook/delete/<int:id>', views.delete_guestbook, name='delete-guestbook'),
]