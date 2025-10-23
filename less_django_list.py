# Джанго с нуля коды и команды пошагово...

# step-1 (first tab)
# Учимся создавать проект джанго-админка на языке пайтон

# python -m venv venv

# venv\Scripts\Activate

# pip install django

# django-admin startproject less_project

# python manage.py startapp students

# INSTALLED_APPS = [
# "students",
# ]

# python manage.py migrate

# python manage.py runserver
# ================================================================================================================================================


# step-2 (second tab)
# Создаем Адимна в джанго-админке и заходим в поле админку

# Новый терминал открываем cmd
# python manage.py createsuperuser

# Username (leave blank to use 'techline'): Abu

# Email address: nazarov3383@gmail.com

# Password: 3383

# Password (again): 3383

# Bypass password validation and create user anyway? [y/N]: y

# http://127.0.0.1:8000/admin

# settings.py ----> LANGUAGE_CODE = "ru"
# ================================================================================================================================================

# step-3 (Third tab)
# Добавляем класс Студенты и группы и меняем настройки

# models.py
# class Student(models.Model):
#     name = models.CharField(verbose_name="Имя студента", max_length=50, null=True, blank=True)
#     surname = models.CharField(verbose_name="Фамилия студента", max_length=50, null=True, blank=True)
#     age = models.IntegerField(verbose_name="Возраст студента", default=12)
#     email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
#     description = models.TextField(verbose_name="Коментарий", null=True, blank=True)
#     group = models.ForeignKey("Group", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Группа")

#     def __str__(self):
#         return f"{self.surname} {self.name} - {self.group.name}"

#     class Meta:
#         verbose_name = "Студент"
#         verbose_name_plural = "Студенты"
#

# class Group(models.Model):
#     name = models.CharField(max_length=100, default="Без имени")

#     def __str__(self):
#         return f"{self.name} - {self.id}"

#     class Meta:
#         verbose_name = "Группа"
#         verbose_name_plural = "Группы"
# ------------------------------------------------------------------------

# admin.py
# from .models import Student, Group

# class StudentAdmin(admin.ModelAdmin):
#     pass

# class GroupAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Student, StudentAdmin)
# admin.site.register(Group, GroupAdmin)
# ------------------------------------------------------------------------

# apps.py
# from django.apps import AppConfig

# class StudentsConfig(AppConfig):
#     default_auto_field = "django.db.models.BigAutoField"
#     name = "students"
#     verbose_name = "Студенты"
# ------------------------------------------------------------------------
# ================================================================================================================================================

# step-4 (Fourth tab)
# Добавляем Телефон, Фото, Дата регистрации

# Телефон
# pip install django-phonenumber-field phonenumbers

# from phonenumber_field.modelfields import PhoneNumberField
# phone_number = PhoneNumberField(verbose_name = "Телефон", region="KG", default="+996000000000")

# INSTALLED_APPS = [
#     "phonenumber_field",
# ]
# ------------------------------------------------------------------------

# Фото
# pip install Pillow

# После Статик
# STATIC_URL = "static/"
# Добавляем
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# Создаем папку media на уровне со всеми папками

# avatar = models.ImageField(upload_to="Фото_студентов", null=True)

# urls.py
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ------------------------------------------------------------------------

# Дата создания и дата обновления
# join_date = models.DateField(verbose_name="Дата присоединения", auto_now_add=True)
# updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

# TIME_ZONE = "Asia/Bishkek"

# admin.py
# class StudentAdmin(admin.ModelAdmin):
#     readonly_fields = ('join_date', 'updated_date')
# ------------------------------------------------------------------------
# ================================================================================================================================================

# step-5 (Fifth tab)
# STATIC and TEMPLATES
# ------

# static
# folder static
# folders: svg, images, css, js
# files: -  -  style.css main.js
# ------

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
# ------

# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from students.views import main, student_detail
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('main/', main),
#     path('students/<int:id>/', student_detail)
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

# ------------------------------------------------------------------------
# templates
# folder templates
# files index.html student_detail.html
# ------

# TEMPLATES = [
#     {
#         "DIRS": [
#             BASE_DIR / 'templates',
#         ],
#     },
# ]
# ------

# from django.shortcuts import render
# from django.http import HttpResponse
# from students.models import Student

# def main(request):
#     # return HttpResponse("Hello, world!")
#     return render(request, "index.html")

# def main(request):
#     students = Student.objects.all()
#     print(students)
#     return render(request, "main/index.html", {"students": students})

# def main(request):
#     students = Student.objects.all()
#     # teachers = Teacher.objects.all()
#     return render(request, "index.html", {
#         "students": students,
#         # "teachers": teachers,
#     })

# def student_detail(request, id):
#     student = Student.objects.get(id=id)
#     print(student)
#     return render(request, 'student_detail.html', {
#         "student": student,
#     })
# ------
# ================================================================================================================================================

# step-6 (sixth tab) Делаем более живую админ-панель
# # Админ-панель

# admin.py
# class StudentAdmin(admin.ModelAdmin):
#     readonly_fields = ('join_date', 'updated_date')
#     list_display = ('id', 'name', 'surname', 'phone_number', 'email', 'number', "avatar_preview",)
#     list_display_links = ('id', 'name', 'surname',)
#     search_fields = ('name', 'group__name', 'surname',)
#     list_filter = ('group__name', 'age',)
#     ordering = ('-join_date', '-updated_date',)
#     list_editable = ('phone_number', 'email', 'number',)
#     reodonaly_fields = ('join_date', 'updated_date',)
#     list_per_page = 5
#     date_hierarchy = 'join_date'
#     fieldsets = (
#         ('Основная информация', {
#             'fields': ('name', 'surname', 'age', 'number', 'phone_number', 'group', 'email', 'description', 'is_active',)
#         }),
#         ('Дополнительная информация', {
#             'fields':('join_date', 'updated_date'),
#             'classes': ('collapse',)
#         })
#     )
#     save_on_top = True

#     @admin.action(description="Активировать пользователя")
#     def make_active(modeladmin, request, queryset):
#         queryset.update(is_active = True)
#     actions = [make_active]

#     # prepopulated_fields = {'surname': ('name',)}
#     # fields = ('name', 'email',)
#     # exclude = ('surname',)
# # ----------------------------------------------------------------------------------------------------

# models.py
# class Student(models.Model):
#     name = models.CharField(verbose_name="Имя футболиста", max_length=50, null=True, blank=True)
#     surname = models.CharField(verbose_name="Фамилия футболиста", max_length=50, null=True, blank=True)
#     age = models.IntegerField(verbose_name="Возраст футболиста", default=18)
#     number = models.IntegerField(verbose_name="Номер футболиста", null=True, blank=True)
#     email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
#     description = models.TextField(verbose_name="Коментарий", max_length=150, null=True, blank=True)
#     group = models.ForeignKey("Group", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Группа")
#     phone_number = PhoneNumberField(verbose_name = "Телефон", region="KG", default="+996000000000")
#     avatar = models.ImageField(upload_to="Фото_футболистов", null=True)
#     join_date = models.DateField(verbose_name="Дата присоединения", auto_now_add=True)
#     updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
#     is_active = models.BooleanField(verbose_name="Активен", default=True)

#     def __str__(self):
#         return f"{self.surname} {self.name} - {self.group.name}"

#     class Meta:
#         verbose_name = "Футболист"
#         verbose_name_plural = "Футболисты"

#     def avatar_preview(self):
#         if self.avatar:
#             return mark_safe(f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:5px"/>')
#         return "—"
#     avatar_preview.short_description = "Аватарка"
# # ------------------------------------------------------------------------
# ================================================================================================================================================

# step-7 (seventh tab)

# urls.py
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from students.views import main, student_detail, create_student

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', main),
#     path('student-create/', create_student, name='create_student'),
#     path('students/<int:id>/', student_detail, name = "student_detail")
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

# -------------------

# index.html
#  <div class="students_container">

#         {% for student in students %}
#             <div class="student_card">
#                 <div>
#                     <a href="{% url 'student_detail' id=student.id %}">
#                         {% if student.avatar %}
#                         <img src="{{ student.avatar.url }}" alt="{{ student.name }}">
#                         {% else %}
#                         No avatar
#                         {% endif %}
#                     </a>
#                 </div>
#                 <div>Имя: {{ student.name}}</div>
#                 <div>Фамилия: {{ student.surname}}</div>
#                 <div>Возраст: {{ student.age}}</div>
#                 <div>Должность: {{ student.group.name}}</div>
#                 <div>Майл: {{ student.email}}</div>
#                 <div>Телефон: {{ student.phone_number}}</div>
#                 <div>Дата создания: {{ student.join_date }}</div>
#                 <div>Дата обновления: {{ student.updated_date }}</div>
#             </div>
#         {%  endfor  %}

#     </div>
# -------------------

# students_create.html
# {% load static %}

# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Django_lessons_3</title>
#     <link rel="stylesheet" href="{% static 'css/style.css' %}" />
#   </head>
#   <body>
#     <h1>Create Student</h1>

#     <div class="student_form">
#       <form action="{% url 'create_student' %}" method="POST">
#         {% csrf_token %}

#         <div class="student_input">
#           <label for="name">Name</label>
#           <input type="text" name="name" />
#         </div>
#         <div class="student_input">
#           <label for="surname">Surame</label>
#           <input type="text" name="surname" />
#         </div>
#         <div class="student_input">
#           <label for="age">Age</label>
#           <input type="number" name="age" />
#         </div>
#         <div class="student_input">
#           <label for="email">Email</label>
#           <input type="email" name="email" />
#         </div>
#         <div class="student_input">
#           <label for="phone_number">Phone number</label>
#           <input type="text" name="phone_number" />
#         </div>
#         <div class="student_input">
#           <label for="avatar">Avatar</label>
#           <input type="file" name="avatar" />
#         </div>
#         <div class="student_input">
#           <select name="group" id="">
#             {% for group in groups %}
#               <option value="{{ group.id }}">{{ group.name }}</option>
#             {% endfor %}
#           </select>
#         </div>
#         <div class="student_from_button">
#           <input type="submit">
#         </div>
#       </form>
#     </div>
#   </body>
# </html>
# -------------------

# students_detail.html
# {% load static %}

# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Django_lessons</title>
#     <link rel="stylesheet" href="{% static 'css/style.css' %}" />
#   </head>
#   <body>
#     <img src="{% static 'svg/real-madrid-c-f.svg' %}" alt="" />

#     <h1>Реал Мадрид</h1>

#     <h2>Результат найденного футболиста...</h2>

#     <div class="student_container">
#       <div class="student_card_detail">
#         <div class="student_image">
#           {% if student.avatar %}
#             <img src="{{ student.avatar.url }}" alt="student.name" />
#           {% else %}
#             No avatar
#           {% endif %}
#         </div>
#         <div>Имя : {{ student.name }}</div>
#         <div>Фамилия : {{ student.surname }}</div>
#         <div>Возраст: {{ student.age }}</div>
#         <div>Должность: {{ student.group.name }}</div>
#         <div>Электронная почта: {{ student.email }}</div>
#         <div>Телефон: {{ student.phone_number }}</div>
#         <div>Описание: {{ student.description }}</div>
#         <div>Дата присоединения: {{ student.join_date }}</div>
#         <div>Дата обновления: {{ student.updated_date }}</div>
#       </div>
#     </div>

#     <script src="{% static 'js/main.js' %}"></script>
#   </body>
# </html>
# -------------------

# veiws.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from students.models import Student, Coach, Group

# def main(request):
#     students = Student.objects.all()
#     teachers = Coach.objects.all()

#     return render(request, "index.html", {
#         "students": students,
#         "teachers": teachers,
#     })


# def student_detail(request, id):
#     student = Student.objects.get(id=id)
#     print(student)

#     return render(request, 'student_detail.html', {
#         "student": student,
#     })


# def create_student(request):
#     # print(request.method)
#     groups = Group.objects.all()

#     if request.method == "POST":
#         # print("Post method")
#         # print(request.POST, type(request.POST))
#         name = request.POST.get("name")
#         surname = request.POST.get("surname")
#         age = request.POST.get("age")
#         phone_number = request.POST.get("phone_number")
#         email = request.POST.get("email")
#         group = int(request.POST.get("group"))

#         print(group, type(group))

#         Student.objects.create(
#             name=name,
#             surname=surname,
#             age=age,
#             phone_number=phone_number,
#             email=email,
#             group_id=group
#         )

#     return render(request, 'student_create.html', context={"groups":groups})
# -------------------

# http://127.0.0.1:8000/student-create/ Проверка

# ================================================================================================================================================
# step-8 (eightth tab) CRUD CREATE READE UPDATE

# views.py
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from students.models import Student, Coach, Group
# from django.core.files.storage import FileSystemStorage

# # def main(request):
# #     # return HttpResponse("Hello, world!")
# #     return render(request, "index.html")

# # def main(request):
# #     students = Student.objects.all()
# #     print(students)
# #     return render(request, "main/index.html", {"students": students})


# def main(request):
#     students = Student.objects.all()
#     teachers = Coach.objects.all()

#     return render(request, "index.html", {
#         "students": students,
#         "teachers": teachers,
#     })
# # ----------------------------------------------------------------------------

# def student_detail(request, id):
#     student = Student.objects.get(id=id)
#     print(student)

#     return render(request, 'student_detail.html', {
#         "student": student,
#     })
# # ----------------------------------------------------------------------------

# def student_update(request, id):
#     student = get_object_or_404(Student, id=id)
#     groups = Group.objects.all()
#     success = False

#     if request.method == "POST":
#         student.name = request.POST.get("name")
#         student.surname = request.POST.get("surname")
#         student.age = request.POST.get("age")
#         student.phone_number = request.POST.get("phone_number")
#         student.email = request.POST.get("email")

#         group = Group.objects.get(id=int(request.POST.get("group")))
#         student.group = group

#         if "avatar" in request.FILES:
#             student.avatar = request.FILES["avatar"]

#         student.save()
#         success = True

#     return render(request, 'student_update.html', {
#         "student": student,
#         "groups": groups,
#         'success': success
#     })
# # ----------------------------------------------------------------------------

# def create_student(request):
#     # print(request.method)
#     groups = Group.objects.all()

#     if request.method == "POST":
#         # print("Post method")
#         # print(request.POST, type(request.POST))
#         name = request.POST.get("name")
#         surname = request.POST.get("surname")
#         age = request.POST.get("age")
#         phone_number = request.POST.get("phone_number")
#         email = request.POST.get("email")
#         group = int(request.POST.get("group"))
#         creat_avatar = request.FILES.get("avatar")

#         if creat_avatar:
#             newsImageSystem = FileSystemStorage(location='media/Фото_футболистов/')
#             file_name = newsImageSystem.save(creat_avatar.name, creat_avatar)
#             avatar_path = f"Фото_футболистов/{file_name}"
#         else:
#             avatar_path = None

#         if creat_group:
#             creat_group = int(creat_group)

#         Student.objects.create(
#             name=name,
#             surname=surname,
#             age=age,
#             phone_number=phone_number,
#             email=email,
#             group_id=group,
#             avatar=avatar_path
#         )

#         return render(request, 'student_create.html', context={"groups":groups, "success": True})

#     return render(request, 'student_create.html', context={"groups":groups})
# # ----------------------------------------------------------------------------


# urls.py

# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from students.views import main, student_detail, create_student, student_update

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', main, name = "main"),
#     path('student-create/', create_student, name='create_student'),
#     path('students/<int:id>/', student_detail, name = "student_detail"),
#     path('students/<int:id>/update', student_update, name = "student_update")
# ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
# # ----------------------------------------------------------------------------

# Templates
# HTML pages and CSS
# # ----------------------------------------------------------------------------
# ================================================================================================================================================
# step-9 (ninth tab) DELETE redirect, get_object_or_404 ()

# urls.py

# from students.views import main, student_detail, create_student, student_update, delete_student
# urlpatterns = [
#     path('students/<int:id>/delete', delete_student, name='delete_student')
# ]
# ----------------------------------------------------------------------------

# views.py
# from django.shortcuts import render, redirect, get_object_or_404

# def delete_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return redirect("/")

# page.html
# <div class="actions">
#     <a href="{% url 'delete_student' id=student.id %}"><button class="delete-btn">Удалить</button></a>
# </div>

# style.css
# .delete-btn {
#     background: #c91019;
#     color: white;
# }
# ----------------------------------------------------------------------------

# base.html

# {% load static %}
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Django_lessons</title>
#     <link rel="stylesheet" href="{% static 'css/style.css' %}">
#   </head>
#   <body>

#     {% include "components/navbar.html" %}

#     {% block content %}

#     {% endblock content %}

#     {% include "components/footer.html" %}

#   </body>
# </html>
# ----------------------------------------------------------------------------
# create folder componenets in folder Template
# and create page.html  1-navbar.html 2-footer.html

# navbar.html
# {% load static %}
# <header>
#   <div class="logo">
#     <img src="{% static 'svg/real-madrid-c-f.svg' %}" alt="" />
#     <h1>Реал Мадрид</h1>
#   </div>

#   <nav class="navigations">
#     <h1>Здесь зона Навигации</h1>
#   </nav>
# </header>
# ----------------------------------------------------------------------------

# footer.html
# {% load static %}
# <footer>
#   <h1>Here zone footer</h1>
# </footer>
# ----------------------------------------------------------------------------
# В остальных html страницах во всех такой же тег

# {% extends 'base.html' %}

# {% load static %}

# {% block content %}

# {% endblock %}
# ----------------------------------------------------------------------------
# ================================================================================================================================================
# step-10 (tenth tab) filter (search)

# navbar.html
#  <form action="{% url 'main' %}" method="GET">
#     <input type="text" name="search" id="" value="{{ search }}" />
#     <input type="submit" />
#   </form>
# # ----------------------------------------------------------------------------

# views.py
# def main(request):
#     students = Student.objects.all()
#     teachers = Coach.objects.all()
#     search = request.GET.get('search')

#     if search:
#         students = Student.objects.filter(name__icontains = search)

#     return render(request, "index.html", {
#         "students": students,
#         "teachers": teachers,
#         "search" : search,
#     })
# # ----------------------------------------------------------------------------
# ================================================================================================================================================
# step-11 pagination
# index.html
# <div>
#       {% if is_paginated %}
#         <div class="pagination">
#           <div class="pagination_btns">
#             {% if students.has_previous %}
#               <a class="page_link" href="?page={{ students.previous_page_number }}"><</a>
#             {% endif %}

#             {% for i in students.paginator.page_range %}
#               {% if students.number == i %}
#                 <span class="page_link">{{ i }}</span>
#               {% else %}
#                 <a class="page_link" href="?page={{ i }}">{{ i }}</a>
#               {% endif %}
#             {% endfor %}

#             {% if students.has_next %}
#               <a class="page_link" href="?page={{ students.next_page_number }}">></a>
#             {% endif %}
#           </div>
#         </div>
#       {% endif %}
#     </div>
# # ----------------------------------------------------------------------------

# views.py
# def main(request):
#     students = Student.objects.all()
#     teachers = Coach.objects.all()
#     search = request.GET.get('search')

#     if search:
#         students = Student.objects.filter(name__icontains = search)

#     page = request.GET.get('page', 1)
#     limit = request.GET.get('limit', 4)

#     paginator = Paginator(students, limit)
#     students = paginator.get_page(page)

#     return render(request, "index.html", {
#         "students": students,
#         "teachers": teachers,
#         "search" : search,
#         "is_paginated": students.has_other_pages()
#     })
# # ----------------------------------------------------------------------------

# style.css
# .pagination{
#     text-aling: center;
# }

# .pagination_btns{
#     margin-top: 70px;
# }

# .page_link{
#     padding: 10px;
#     border: 1px solid;
#     margin: 0 10 px;
# }

# ================================================================================================================================================
# step-12 form
# views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator
# from students.models import Student, Coach, Group
# from students.forms import StudentForm, StudentModelForm


# # Главная страница
# def main(request):
#     students = Student.objects.all()
#     teachers = Coach.objects.all()
#     search = request.GET.get("search")

#     if search:
#         students = students.filter(name__icontains=search)

#     paginator = Paginator(students, 4)
#     page_number = request.GET.get("page")
#     students = paginator.get_page(page_number)

#     return render(
#         request,
#         "index.html",
#         {
#             "students": students,
#             "teachers": teachers,
#             "search": search,
#             "is_paginated": students.has_other_pages(),
#         },
#     )


# # Детали студента
# def student_detail(request, id):
#     student = get_object_or_404(Student, id=id)
#     return render(request, "student_detail.html", {"student": student})


# # Создание нового студента
# def create_student(request):
#     if request.method == "POST":
#         form = StudentModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.save()
#             form.save_m2m()  # сохраняем ManyToMany (tags)
#             return redirect("main")
#     else:
#         form = StudentModelForm()

#     return render(request, "student_create.html", {"form": form})


# # Обновление студента
# def student_update(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == "POST":
#         form = StudentModelForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect("student_detail", id=student.id)
#     else:
#         form = StudentModelForm(instance=student)

#     return render(request, "student_update.html", {"form": form, "student": student})


# # Удаление студента
# def delete_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return redirect("main")
# # ----------------------------------------------------------------------------
# # ------------------------------------------------------------------------
# forms.py
# from django import forms
# from students.models import Student, Group, Tag


# class StudentForm(forms.Form):
#     name = forms.CharField(
#         label="Имя студента", widget=forms.TextInput(attrs={"class": "student_input"})
#     )
#     surname = forms.CharField(
#         label="Фамилия студента",
#         widget=forms.TextInput(attrs={"class": "student_input"}),
#     )
#     age = forms.IntegerField(
#         label="Возраст студента",
#         widget=forms.TextInput(attrs={"class": "student_input"}),
#     )
#     number = forms.IntegerField(
#         label="Номер футболиста",
#         required=False,
#         widget=forms.TextInput(attrs={"class": "student_input"}),
#     )
#     email = forms.EmailField(
#         label="Электронная почта",
#         widget=forms.TextInput(attrs={"class": "student_input"}),
#     )
#     phone_number = forms.CharField(
#         label="Номер телефона", widget=forms.TextInput(attrs={"class": "student_input"})
#     )
#     group = forms.ModelChoiceField(label="Группа", queryset=Group.objects.all())
#     description = forms.CharField(
#         label="Комментарий",
#         required=False,
#         widget=forms.Textarea(attrs={"class": "student_input", "rows": 3}),
#     )
#     avatar = forms.ImageField(
#         label="Аватарка",
#         required=False,
#         widget=forms.ClearableFileInput(attrs={"class": "student_input"}),
#     )
#     is_active = forms.BooleanField(label="Активен", required=False)
#     tags = forms.ModelMultipleChoiceField(
#         label="Теги",
#         queryset=Tag.objects.all(),
#         required=False,
#         widget=forms.SelectMultiple(attrs={"class": "student_input"}),
#     )


# class StudentModelForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = (
#             "name",
#             "surname",
#             "age",
#             "number",
#             "email",
#             "phone_number",
#             "group",
#             "description",
#             "avatar",
#             "is_active",
#             "tags",
#         )
#         labels = {
#             "name": "Имя студента",
#             "surname": "Фамилия студента",
#             "age": "Возраст студента",
#             "number": "Номер футболиста",
#             "email": "Электронная почта",
#             "phone_number": "Номер телефона",
#             "group": "Группа",
#             "description": "Комментарий",
#             "avatar": "Аватарка",
#             "is_active": "Активен",
#             "tags": "Теги",
#         }
#         widgets = {
#             "avatar": forms.ClearableFileInput(attrs={"class": "student_input"}),
#             "description": forms.Textarea(attrs={"class": "student_input", "rows": 3}),
#             "tags": forms.SelectMultiple(attrs={"class": "student_input"}),
#         }
# # # ----------------------------------------------------------------------------
# # ------------------------------------------------------------------------
# models.py
# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# from django.utils.html import mark_safe


# class Group(models.Model):
#     name = models.CharField(max_length=100, default="Без имени")

#     def __str__(self):
#         return f"{self.name} - {self.id}"

#     class Meta:
#         verbose_name = "Должность"
#         verbose_name_plural = "Должности"
# # ------------------------------------------------------------------------

# class Tag(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.name} - {self.id}"

#     class Meta:
#         verbose_name = "Тег"
#         verbose_name_plural = "Теги"


# class Student(models.Model):
#     name = models.CharField(verbose_name="Имя футболиста", max_length=50, null=True, blank=True)
#     surname = models.CharField(verbose_name="Фамилия футболиста", max_length=50, null=True, blank=True)
#     age = models.IntegerField(verbose_name="Возраст футболиста",  null=True, blank=True)
#     number = models.IntegerField(verbose_name="Номер футболиста", null=True, blank=True)
#     email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
#     description = models.TextField(verbose_name="Коментарий", max_length=150, null=True, blank=True)
#     group = models.ForeignKey("Group", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Группа")
#     phone_number = PhoneNumberField(verbose_name = "Телефон", region="KG", default="+996000000000")
#     avatar = models.ImageField(upload_to="Фото_футболистов", null=True)
#     join_date = models.DateField(verbose_name="Дата присоединения", auto_now_add=True)
#     updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
#     is_active = models.BooleanField(verbose_name="Активен", default=True)
#     tags = models.ManyToManyField(Tag, related_name="students")

#     def __str__(self):
#         return f"{self.surname} {self.name} - {self.age}"

#     class Meta:
#         verbose_name = "Футболист"
#         verbose_name_plural = "Футболисты"

#     def avatar_preview(self):
#         if self.avatar:
#             return mark_safe(f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:5px"/>')
#         return "—"
#     avatar_preview.short_description = "Аватарка"
# # ------------------------------------------------------------------------

# class Coach(models.Model):
#     name = models.CharField(verbose_name="Имя тренера", max_length=50, null=True, blank=True)
#     surname = models.CharField(verbose_name="Фамилия тренера", max_length=50, null=True, blank=True)
#     age = models.IntegerField(verbose_name="Возраст тренера", default=12)
#     email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
#     description = models.TextField(verbose_name="Коментарий", max_length=150, null=True, blank=True)
#     group = models.ForeignKey("Group", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Группа")
#     phone_number = PhoneNumberField(verbose_name = "Телефон", region="KG", default="+996000000000")
#     avatar = models.ImageField(upload_to="Фото_тренеров", null=True)
#     join_date = models.DateField(verbose_name="Дата присоединения", auto_now_add=True)
#     updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
#     is_active = models.BooleanField(verbose_name="Активен", default=True)

#     def __str__(self):
#         return f"{self.surname} {self.name}"

#     class Meta:
#         verbose_name = "Тренер"
#         verbose_name_plural = "Тренеры"

#     def avatar_preview(self):
#         if self.avatar:
#             return mark_safe(f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:5px"/>')
#         return "Нету аватара"
#     avatar_preview.short_description = "Аватарка"
# # ------------------------------------------------------------------------
# # ------------------------------------------------------------------------
# admins.py
# from django.contrib import admin
# from .models import Student, Group, Coach, Tag


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     readonly_fields = ("join_date", "updated_date")
#     list_display = (
#         "id",
#         "name",
#         "surname",
#         "phone_number",
#         "email",
#         "number",
#         "avatar_preview",
#     )
#     list_display_links = ("id", "name", "surname")
#     search_fields = ("name", "surname", "group__name")
#     list_filter = ("group__name", "age", "is_active", "tags")
#     ordering = ("-join_date", "-updated_date")
#     list_editable = ("phone_number", "email", "number")
#     list_per_page = 5
#     date_hierarchy = "join_date"
#     filter_horizontal = ("tags",)

#     fieldsets = (
#         (
#             "Основная информация",
#             {
#                 "fields": (
#                     "name",
#                     "surname",
#                     "age",
#                     "number",
#                     "phone_number",
#                     "group",
#                     "email",
#                     "description",
#                     "is_active",
#                     "tags",
#                 )
#             },
#         ),
#         (
#             "Дополнительная информация",
#             {"fields": ("join_date", "updated_date"), "classes": ("collapse",)},
#         ),
#     )

#     save_on_top = True

#     @admin.action(description="Активировать пользователя")
#     def make_active(modeladmin, request, queryset):
#         queryset.update(is_active=True)

#     actions = [make_active]


# @admin.register(Coach)
# class CoachAdmin(admin.ModelAdmin):
#     readonly_fields = ("join_date", "updated_date")
#     list_display = ("id", "name", "surname", "email", "phone_number", "avatar_preview")
#     list_display_links = ("id", "name", "surname")
#     search_fields = ("name", "surname")
#     list_filter = ("age", "is_active")
#     list_editable = ("phone_number", "email")
#     list_per_page = 5
#     ordering = ("-join_date", "-updated_date")
#     save_on_top = True

#     fieldsets = (
#         (
#             "Основная информация",
#             {
#                 "fields": (
#                     "name",
#                     "surname",
#                     "age",
#                     "phone_number",
#                     "group",
#                     "email",
#                     "description",
#                     "is_active",
#                 )
#             },
#         ),
#         (
#             "Дополнительная информация",
#             {"fields": ("join_date", "updated_date"), "classes": ("collapse",)},
#         ),
#     )

#     @admin.action(description="Активировать пользователя")
#     def make_active(modeladmin, request, queryset):
#         queryset.update(is_active=True)

#     actions = [make_active]


# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ("id", "name")
#     search_fields = ("name",)


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ("id", "name")
#     search_fields = ("name",)
# ================================================================================================================================================
# FILTER

# filter.py
# import django_filters

# from .models import Student, Group, Tag
# from django import forms


# class StudentFilter(django_filters.FilterSet):
#     # name = django_filters.CharFilter(lookup_expr="icontains", label="Имя студента")
#     group = django_filters.ModelChoiceFilter(
#         queryset=Group.objects.all(), widget=forms.Select, empty_label="Выбрать группу",
#     )

#     tags = django_filters.ModelMultipleChoiceFilter(
#         queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple
#     )

#     class Meta:
#         model = Student
#         fields = ( "age", "group", "tags")
# --------------------------------------------------------------------

# html
# <div>
#       <h2>Фильтр студентов</h2>
#       <form method="GET">
#         {% csrf_token %}
#         {{ filter.form.as_div }}

#         <div class="actions">
#           <button class="create-btn">Фильтр</button>
#         </div>
#       </form>
#     </div>
# --------------------------------------------------------------------
# settings

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "students",
#     "phonenumber_field",
#     "django_filters",
# ]
# ================================================================================================================================================
# views.py
# from django.shortcuts import render

# def my_view(request):
#     # Получаем URL предыдущей страницы, если нет — используем "/"
#     referer = request.META.get('HTTP_REFERER', '/')
#     return render(request, 'my_template.html', {'referer': referer})
# ------------------------------------------------------------------------------------

# html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Пример Previous Page</title>
# </head>
# <body>
#     <h1>Текущая страница</h1>
#     <a href="{{ referer }}"><button>Назад</button></a>
# </body>
# </html>

# ================================================================================================================================================
# Добавить новый тег
# Добавить новую группу
# html
# <div class="extra-links">
#           <a href="{% url 'create_group' %}"><button type="button" class="create-btn">➕ Добавить новую группу</button></a>
#           <a href="{% url 'create_tag' %}"><button type="button" class="create-btn">➕ Добавить новый тег</button></a>
#         </div>

# ------------------------------------------------------------------------------------
# Page create_group or create_tag html

# {% extends 'base.html' %}
# {% load static %}

# {% block content %}
#   <h1>Добавить новую группу</h1>

#   <div class="container">
#     <a href="{% url 'create_student' %}">
#       <button class="back-btn">⬅ Назад</button>
#     </a>
#   </div>

#   <div class="student_form">
#     <form method="POST">
#       {% csrf_token %}
#       {{ form.as_p }}
#       <button type="submit" class="submit-btn">Создать группу</button>
#     </form>
#   </div>
# {% endblock %}
# ------------------------------------------------------------------------------------
# views.py
# Создание новой группы
# def create_group(request):
#     if request.method == "POST":
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("create_student")  # возвращаемся на создание студента
#     else:
#         form = GroupForm()
#     return render(request, "create_group.html", {"form": form})


# # Создание нового тега
# def create_tag(request):
#     if request.method == "POST":
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("create_student")  # возвращаемся на создание студента
#     else:
#         form = TagForm()
#     return render(request, "create_tag.html", {"form": form})
# ------------------------------------------------------------------------------------
# forms.py
# class GroupForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         fields = ["name"]
#         labels = {"name": "Название группы"}
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "student_input"}),
#         }


# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ["name"]
#         labels = {"name": "Название тега"}
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "student_input"}),
#         }
# ------------------------------------------------------------------------------------
# urls.py

# path("create-group/", create_group, name="create_group"),
# path("create-tag/", create_tag, name="create_tag"),
# ================================================================================================================================================
# Git and GitHub
# Скачиваем Git и Устанавливаем GitBash (Обращаем внимание при установке при выборе компонентов)
# Создаем аккаунт на GitHub
# И сщздаем новый репозиторий
# Важно отметить .gitignore - python

# Создаем новый файл .gitignore - (есть готовый шаблон вставляем (особенно: venv venv/ migrations migrations/ __pycache__))
# Не забываем requirements.txt

# git init
# git add .
# git commit -m "first commit"
# git branch -M main
# git remove add origin https://github.com/
# git push-u orrigin main

# далее будут еще команды приобновлении по GutHub
# ================================================================================================================================================
# Не забываем лайфхаки

# 1. empty_label = "Выбрать"


# ================================================================================================================================================
# CBV
# urls.py (local)

# from django.urls import path
# from students.views import (
#     StudentListView,
#     StudentDetailView,
#     StudentUpdateView,
#     StudentDeleteView,
#     StudentCreateView,
#     GroupCreateView,
#     TagCreateView,
# )

# urlpatterns = [
#     # Students
#     path("", StudentListView.as_view(), name="main"),
#     path("students/create/", StudentCreateView.as_view(), name="create_student"),
#     path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
#     path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
#     path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),

#     # Groups & Tags
#     path("groups/create/", GroupCreateView.as_view(), name="create_group"),
#     path("tags/create/", TagCreateView.as_view(), name="create_tag"),
# ]

# urls.py (global)
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [path("admin/", admin.site.urls), path("", include("students.urls"))]

# # Static & Media
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ------------------------------------------------------------------------------------------------------------------------------------------
# views Дженерик
# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from students.models import Student, Group, Tag
# from students.forms import StudentModelForm, GroupForm, TagForm
# from students.filters import StudentFilter

# # ===============================
# # Список студентов с фильтром и пагинацией
# # ===============================
# class StudentListView(ListView):
#     model = Student
#     template_name = "index.html"
#     context_object_name = "students"
#     paginate_by = 3  # студентов на одной странице

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = StudentFilter(self.request.GET, queryset=queryset)
#         return self.filterset.qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = self.filterset
#         return context


# # ===============================
# # Детали студента
# # ===============================
# class StudentDetailView(DetailView):
#     model = Student
#     template_name = "student_detail.html"
#     context_object_name = "student"


# # ===============================
# # Создание студента
# # ===============================
# class StudentCreateView(CreateView):
#     model = Student
#     form_class = StudentModelForm
#     template_name = "student_create.html"
#     success_url = reverse_lazy("main")


# # ===============================
# # Обновление студента
# # ===============================
# class StudentUpdateView(UpdateView):
#     model = Student
#     form_class = StudentModelForm
#     template_name = "student_update.html"

#     def get_success_url(self):
#         return reverse_lazy("student_detail", kwargs={"pk": self.object.pk})


# # ===============================
# # Удаление студента
# # ===============================
# class StudentDeleteView(DeleteView):
#     model = Student
#     template_name = "student_confirm_delete.html"
#     success_url = reverse_lazy("main")


# # ===============================
# # Создание группы
# # ===============================
# class GroupCreateView(CreateView):
#     model = Group
#     form_class = GroupForm
#     template_name = "create_group.html"
#     success_url = reverse_lazy("create_student")


# # ===============================
# # Создание тега
# # ===============================
# class TagCreateView(CreateView):
#     model = Tag
#     form_class = TagForm
#     template_name = "create_tag.html"
#     success_url = reverse_lazy("create_student")
# ----------------------------------------------------------------
# Кастомный views

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from students.models import Student, Group
# from students.forms import StudentModelForm, GroupForm, TagForm
# from django.views.generic import ListView

# # ===============================
# # Список студентов
# # ===============================
# class StudentView(ListView):
#     def get(self, request):
#         students = Student.objects.all()
#         return render(request, "index.html", {"students": students})

#     def post(self, request):
#         name = request.POST.get("name")
#         Student.objects.create(name=name)
#         return redirect("main")


# # ===============================
# # Детали студента
# # ===============================
# class StudentDetailView(ListView):
#     def get(self, request, id):
#         student = get_object_or_404(Student, id=id)
#         return render(request, "student_detail.html", {"student": student})


# # ===============================
# # Обновление студента
# # ===============================
# class StudentUpdateView(ListView):
#     def get(self, request, id):
#         student = get_object_or_404(Student, id=id)
#         form = StudentModelForm(instance=student)
#         return render(
#             request, "student_update.html", {"form": form, "student": student}
#         )

#     def post(self, request, id):
#         student = get_object_or_404(Student, id=id)
#         form = StudentModelForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect("student_detail", id=student.id)
#         return render(
#             request, "student_update.html", {"form": form, "student": student}
#         )


# # ===============================
# # Удаление студента
# # ===============================
# class StudentDeleteView(ListView):
#     def get(self, request, id):
#         student = get_object_or_404(Student, id=id)
#         student.delete()
#         return redirect("main")


# # ===============================
# # Создание студента
# # ===============================
# class StudentCreateView(ListView):
#     def get(self, request):
#         form = StudentModelForm()
#         return render(request, "student_create.html", {"form": form})

#     def post(self, request):
#         form = StudentModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.save()
#             form.save_m2m()
#             return redirect("main")
#         return render(request, "student_create.html", {"form": form})


# # ===============================
# # Создание группы
# # ===============================
# class GroupCreateView(ListView):
#     def get(self, request):
#         form = GroupForm()
#         return render(request, "create_group.html", {"form": form})

#     def post(self, request):
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("create_student")  # после создания — к форме студента
#         return render(request, "create_group.html", {"form": form})


# # ===============================
# # Создание тега
# # ===============================
# class TagCreateView(ListView):
#     def get(self, request):
#         form = TagForm()
#         return render(request, "create_tag.html", {"form": form})

#     def post(self, request):
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("create_student")  # после создания — к форме студента
#         return render(request, "create_tag.html", {"form": form})
# ---------------------------------------------------------------------------------------------------
# html
# student.pk
# # ============================================================================================================================
# template.views
# Изменения в templates то есть отдель создаем student_list.html about.html (учитывая пагинацию и фильтр)
# Изменения в настройках views.py

# # ============================================================================================================================
# signals.py
# Создаем signals.py
# Изменения в настройках models.py views.py apps.py
# (можно без специальной страницы оплаты)

# # ============================================================================================================================

# 21.10.2025
# Auth Авторизация
