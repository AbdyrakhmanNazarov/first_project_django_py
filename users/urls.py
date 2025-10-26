from django.urls import path
from .views import create_user, user_list, edit_user, delete_user

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('list/', user_list, name='user_list'),
    path('edit/<int:user_id>/', edit_user, name='edit_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
