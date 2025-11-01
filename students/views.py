from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from students.models import Student
from students.filters import StudentFilter


# ===============================
# Главная страница (открыта для всех)
# ===============================
class MainTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filterset = StudentFilter(self.request.GET, queryset=Student.objects.all())
        students_list = filterset.qs

        paginator = Paginator(students_list, 3)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        # Получаем лайки и корзину из сессии
        liked_students = self.request.session.get("liked_students", [])
        cart = self.request.session.get("cart", [])

        context.update({
            "students": page_obj,
            "page_obj": page_obj,
            "paginator": paginator,
            "is_paginated": page_obj.has_other_pages(),
            "filter": filterset,
            "title": "Главная страница",
            "liked_students": liked_students,
            "cart": cart,
        })
        return context


# ===============================
# About страница
# ===============================
class AboutTemplateView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Page"
        return context


# ===============================
# Contacts страница
# ===============================
class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contacts Page"
        return context


# ===============================
#  Лайки студентов (через session)
# ===============================
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
    return redirect(request.META.get('HTTP_REFERER', 'home')) 


# ===============================
#  Корзина студентов (через session)
# ===============================
def add_to_cart(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    cart = request.session.get("cart", [])

    if student_id not in cart:
        cart.append(student_id)
        messages.success(request, f"{student.name} добавлен в корзину!")
    else:
        messages.info(request, f"{student.name} уже в корзине.")

    request.session["cart"] = cart
    return redirect(request.META.get('HTTP_REFERER', 'home')) 


# ===============================
#  Просмотр корзины
# ===============================
def cart_view(request):
    cart_ids = request.session.get("cart", [])
    students_in_cart = Student.objects.filter(id__in=cart_ids)
    return render(
        request,
        "cart.html",
        {"students": students_in_cart, "title": "Ваша корзина"},
    )


# ===============================
#  Очистить корзину
# ===============================
def clear_cart(request):
    request.session["cart"] = []
    messages.info(request, "Корзина очищена!")
    return redirect('cart_view')
