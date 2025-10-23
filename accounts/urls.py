from django.urls import path
from .views import login_acc, logout_acc, register_acc

urlpatterns = [
    path("login/", login_acc, name="login_acc"),       # страница логина
    path("logout/", logout_acc, name="logout_acc"),   # выход из аккаунта
    path("register/", register_acc, name="register_acc"),  # регистрация
]
