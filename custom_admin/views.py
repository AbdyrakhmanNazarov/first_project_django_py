from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator

from custom_admin.forms import StudentModelForm, GroupForm, TagForm, PaymentForm
from students.models import Student, Group, Tag, StudentContract
from students.filters import StudentFilter

# ===============================
# Cookie
# ===============================
@login_required(login_url="login_acc")
def set_cookie_view(request):
    response = redirect("admin_view") 
    response.set_cookie("username", request.user.username, max_age=3600)
    messages.success(request, f"Кука установлена для {request.user.username}!")
    return response

@login_required(login_url="login_acc")
def get_cookie_view(request):
    username = request.COOKIES.get("username", "Гость")
    messages.info(request, f"Привет, {username}")
    return redirect("admin_view")

@require_POST
@login_required(login_url="login_acc")
def delete_cookie_view(request):
    response = redirect("admin_view")
    response.delete_cookie("username")
    messages.warning(request, f"Кука удалена для {request.user.username}!")
    return response

# ===============================
# Session
# ===============================
@login_required(login_url="login_acc")
def set_session_view(request):
    request.session["username"] = request.user.username
    request.session["user_id"] = request.user.id
    messages.success(request, f"Сессия установлена для {request.user.username}!")
    return redirect("admin_view")

@login_required(login_url="login_acc")
def get_session_view(request):
    username = request.session.get("username", "Гость")
    user_id = request.session.get("user_id", "неизвестно")
    messages.info(request, f"Имя: {username}, ID: {user_id}")
    return redirect("admin_view")

@login_required(login_url="login_acc")
def visit_counter(request):
    username = request.user.username
    visit = request.session.get("visit", 0)
    request.session["visit"] = visit + 1
    messages.info(request, f"Вы {username}, заходили на эту страницу {visit + 1} раз")
    return redirect("admin_view")

@require_POST
@login_required(login_url="login_acc")
def delete_session_view(request):
    request.session.flush()
    messages.warning(request, f"Сессия очищена для {request.user.username}!")
    return redirect("admin_view")


# ===============================
# Личный кабинет (CRUD студентов)
# ===============================
class StudentListView(LoginRequiredMixin, ListView):
    login_url = "login_acc"
    model = Student
    template_name = "custom_admin/student_list.html"
    context_object_name = "students"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = StudentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"filter": self.filterset, "title": "Личный кабинет"})
        return context

class StudentDetailView(LoginRequiredMixin, DetailView):
    login_url = "login_acc"
    model = Student
    template_name = "custom_admin/student_detail.html"
    context_object_name = "student"

class StudentCreateView(LoginRequiredMixin, CreateView):
    login_url = "login_acc"
    model = Student
    form_class = StudentModelForm
    template_name = "custom_admin/student_create.html"
    success_url = reverse_lazy("student_list")

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "login_acc"
    model = Student
    form_class = StudentModelForm
    template_name = "custom_admin/student_update.html"

    def get_success_url(self):
        return reverse_lazy(
            "custom_admin/student_detail", kwargs={"pk": self.object.pk}
        )

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "login_acc"
    model = Student
    template_name = "custom_admin/student_confirm_delete.html"
    success_url = reverse_lazy("custom_admin/student_list")

class GroupCreateView(LoginRequiredMixin, CreateView):
    login_url = "login_acc"
    model = Group
    form_class = GroupForm
    template_name = "custom_admin/create_group.html"
    success_url = reverse_lazy("custom_admin/create_student")

class TagCreateView(LoginRequiredMixin, CreateView):
    login_url = "login_acc"
    model = Tag
    form_class = TagForm
    template_name = "custom_admin/create_tag.html"
    success_url = reverse_lazy("custom_admin/create_student")

# ===============================
# Оплата студентов
# ===============================
@login_required(login_url="login_acc")
def student_payment_page(request, pk):
    contract = get_object_or_404(StudentContract, pk=pk)
    form = PaymentForm(instance=contract)
    return render(
        request,
        "custom_admin/student_payment.html",
        {"contract": contract, "form": form},
    )

@login_required(login_url="login_acc")
@require_POST
def student_payment_view(request, pk):
    contract = get_object_or_404(StudentContract, pk=pk)
    form = PaymentForm(request.POST, instance=contract)

    if form.is_valid():
        form.save()
        messages.success(
            request,
            f"Оплата {form.cleaned_data['amount']} успешно проведена для {contract.student.name}.",
        )
    else:
        messages.error(request, "Не удалось провести оплату. Проверьте сумму.")

    return redirect("custom_admin/student_list")


# ===============================
# Кастомная админка
# ===============================
class MainAdminView(TemplateView):
    template_name = "custom_admin/main.html"


# ===============================
# Главная страница сайта (лайки + корзина)
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


# ==============================
#  Лайки студентов
# ==============================
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
    return redirect("home")


# ===============================
# Корзина студентов
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
    return redirect("home")


def cart_view(request):
    cart_ids = request.session.get("cart", [])
    students_in_cart = Student.objects.filter(id__in=cart_ids)
    return render(
        request,
        "cart.html",
        {"students": students_in_cart, "title": "Ваша корзина"},
    )


def clear_cart(request):
    request.session["cart"] = []
    messages.info(request, "Корзина очищена!")
    return redirect("cart_view")
