from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from students.models import Student, Group, Tag, StudentContract
from students.forms import StudentModelForm, GroupForm, TagForm, PaymentForm
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

        context.update({
            "students": page_obj,
            "page_obj": page_obj,
            "paginator": paginator,
            "is_paginated": page_obj.has_other_pages(),
            "filter": filterset,
            "title": "Главная страница"
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
# Личный кабинет (только авторизованные)
# ===============================
class StudentListView(LoginRequiredMixin, ListView):
    login_url = 'login_acc'
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = StudentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "filter": self.filterset,
            "title": "Личный кабинет"
        })
        return context


# ===============================
# Детали студента
# ===============================
class StudentDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login_acc'
    model = Student
    template_name = "student_detail.html"
    context_object_name = "student"


# ===============================
# Создание студента
# ===============================
class StudentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login_acc'
    model = Student
    form_class = StudentModelForm
    template_name = "student_create.html"
    success_url = reverse_lazy("student_list")


# ===============================
# Обновление студента
# ===============================
class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login_acc'
    model = Student
    form_class = StudentModelForm
    template_name = "student_update.html"

    def get_success_url(self):
        return reverse_lazy("student_detail", kwargs={"pk": self.object.pk})


# ===============================
# Удаление студента
# ===============================
class StudentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login_acc'
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy("student_list")


# ===============================
# Создание группы
# ===============================
class GroupCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login_acc'
    model = Group
    form_class = GroupForm
    template_name = "create_group.html"
    success_url = reverse_lazy("create_student")


# ===============================
# Создание тега
# ===============================
class TagCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login_acc'
    model = Tag
    form_class = TagForm
    template_name = "create_tag.html"
    success_url = reverse_lazy("create_student")


# ===============================
# Страница оплаты студента (GET)
# ===============================
@login_required(login_url='login_acc')
def student_payment_page(request, pk):
    contract = get_object_or_404(StudentContract, pk=pk)
    form = PaymentForm(instance=contract)
    return render(request, "student_payment.html", {"contract": contract, "form": form})


# ===============================
# Обработка оплаты студента (POST)
# ===============================
@login_required(login_url='login_acc')
@require_POST
def student_payment_view(request, pk):
    contract = get_object_or_404(StudentContract, pk=pk)
    form = PaymentForm(request.POST, instance=contract)

    if form.is_valid():
        form.save()
        messages.success(
            request,
            f"Оплата {form.cleaned_data['amount']} успешно проведена для {contract.student.name}."
        )
    else:
        messages.error(request, "Не удалось провести оплату. Проверьте сумму.")

    return redirect("student_list")
