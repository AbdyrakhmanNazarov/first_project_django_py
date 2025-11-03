from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from students.models import Student
from django.core.paginator import Paginator

# ================================
# User Page (CRUD + список)
# ================================
@login_required(login_url="login_acc")
def user_page(request):
    students = Student.objects.all().order_by("-join_date")
    paginator = Paginator(students, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    liked_students = request.session.get("liked_students", [])
    cart = request.session.get("cart", [])

    return render(request, "users/user_page.html", {
        "students": page_obj,
        "liked_students": liked_students,
        "cart": cart,
        "page_obj": page_obj,
        "title": "Ваш кабинет"
    })

# ================================
# Лайки студентов
# ================================
@login_required(login_url="login_acc")
def toggle_like(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    liked = request.session.get("liked_students", [])

    if student_id in liked:
        liked.remove(student_id)
        messages.info(request, f"Вы убрали лайк у {student.name}")
    else:
        liked.append(student_id)
        messages.success(request, f"Вы поставили лайк {student.name}")

    request.session["liked_students"] = liked
    return redirect("users:user_page")

# ================================
# Корзина студентов
# ================================
@login_required(login_url="login_acc")
def add_to_cart(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    cart = request.session.get("cart", [])

    if student_id not in cart:
        cart.append(student_id)
        messages.success(request, f"{student.name} добавлен в корзину!")
    else:
        messages.info(request, f"{student.name} уже в корзине.")

    request.session["cart"] = cart
    return redirect("users:user_page")

@login_required(login_url="login_acc")
def cart_view(request):
    cart_ids = request.session.get("cart", [])
    students_in_cart = Student.objects.filter(id__in=cart_ids)
    return render(request, "users/cart.html", {
        "students": students_in_cart,
        "title": "Ваша корзина"
    })

@require_POST
@login_required(login_url="login_acc")
def clear_cart(request):
    request.session["cart"] = []
    messages.info(request, "Корзина очищена!")
    return redirect("users:cart_view")

# ================================
# Просмотр лайков пользователя
# ================================
@login_required(login_url="login_acc")
def liked_students_view(request):
    liked_ids = request.session.get("liked_students", [])
    students_liked = Student.objects.filter(id__in=liked_ids)
    return render(request, "users/liked_students.html", {
        "students": students_liked,
        "title": "Ваши лайки"
    })
