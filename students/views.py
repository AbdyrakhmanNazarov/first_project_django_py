from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from students.models import Student, Coach, Group
from students.forms import StudentForm, StudentModelForm, GroupForm, TagForm
from students.filters import StudentFilter


# Главная страница
def main(request):
    students = Student.objects.all()
    teachers = Coach.objects.all()
    search = request.GET.get("search")

    if search:
        students = students.filter(name__icontains=search)

    filter_set = StudentFilter(request.GET, queryset=students)

    paginator = Paginator(filter_set.qs, 4)
    page_number = request.GET.get("page")
    students = paginator.get_page(page_number)

    return render(
        request,
        "index.html",
        {
            "students": students,
            "teachers": teachers,
            "search": search,
            "is_paginated": students.has_other_pages(),
            "filter": filter_set,
        },
    )


# Детали студента
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "student_detail.html", {"student": student})


# Создание нового студента
def create_student(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()  # сохраняем ManyToMany (tags)
            return redirect("main")
    else:
        form = StudentModelForm()

    return render(request, "student_create.html", {"form": form})


# Обновление студента
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_detail", id=student.id)
    else:
        form = StudentModelForm(instance=student)

    return render(request, "student_update.html", {"form": form, "student": student})


# Удаление студента
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("main")


# Создание новой группы
def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_student")  # возвращаемся на создание студента
    else:
        form = GroupForm()
    return render(request, "create_group.html", {"form": form})


# Создание нового тега
def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_student")  # возвращаемся на создание студента
    else:
        form = TagForm()
    return render(request, "create_tag.html", {"form": form})
