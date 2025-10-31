from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .filters import UserFilterForm
from django.core.paginator import Paginator

@login_required
def user_list(request):
    if not request.user.is_superuser:
        messages.error(request, "Доступ запрещен")
        return redirect("admin_dashboard")

    form = UserFilterForm(request.GET or None)
    users = User.objects.all().order_by("id") 

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        if username:
            users = users.filter(username__icontains=username)
        if email:
            users = users.filter(email__icontains=email)

    paginator = Paginator(users, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "users/user_list.html", {
        "form": form,
        "page_obj": page_obj
    })

@login_required
def create_user(request):
    if not request.user.is_superuser:
        messages.error(request, "Доступ запрещен")
        return redirect("admin_dashboard")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно создан")
            return redirect("user_list")
    else:
        form = CustomUserCreationForm()

    return render(request, "users/create_user.html", {"form": form})


@login_required
def edit_user(request, user_id):
    if not request.user.is_superuser:
        messages.error(request, "Доступ запрещен")
        return redirect("admin_dashboard")

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно обновлен")
            return redirect("user_list")
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, "users/edit_user.html", {"form": form, "user": user})


@login_required
def delete_user(request, user_id):
    if not request.user.is_superuser:
        messages.error(request, "Доступ запрещен")
        return redirect("admin_dashboard")

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()
        messages.success(request, "Пользователь удален")
        return redirect("user_list")

    return render(request, "users/confirm_delete.html", {"user": user})
