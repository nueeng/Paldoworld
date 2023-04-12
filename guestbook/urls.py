from django.urls import path
from . import views

urlpatterns = [
    path('guestbook/', views.guestbook, name='guestbook'),
    path('edit_guestbook/<int:id>', views.edit_guestbook, name='edit-guestbook'),
    path('delete_guestbook/<int:id>', views.delete_guestbook, name='delete-guestbook'),
    path('guestbook/<str:username>/', views.view_guestbook, name='view-guestbook'),

]