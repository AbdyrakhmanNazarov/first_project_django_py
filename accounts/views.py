from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# ===============================
# Авторизация
# ===============================
def login_acc(request):
    if request.user.is_authenticated:
        return redirect("student_list") 

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect("student_list") 
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")

    return render(request, "auth/login.html")


# ===============================
# Выход из аккаунта
# ===============================
def logout_acc(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")
    return redirect("login_acc")  


# ===============================
# Регистрация нового пользователя
# ===============================
def register_acc(request):
    if request.user.is_authenticated:
        return redirect("student_list") 

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Пользователь {user.username} успешно создан! Войдите в аккаунт.")
            return redirect("login_acc")
        else:
            messages.error(request, "Ошибка при создании пользователя. Проверьте форму.")
    else:
        form = UserCreationForm()

    return render(request, "auth/register.html", {"form": form})
