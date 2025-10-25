from django.urls import path
from .views import login_acc, logout_acc, register_acc

urlpatterns = [
    path("login/", login_acc, name="login_acc"),      
    path("logout/", logout_acc, name="logout_acc"),  
    path("register/", register_acc, name="register_acc"),  
]
