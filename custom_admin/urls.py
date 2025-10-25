from django.urls import path
from custom_admin.views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    GroupCreateView,
    TagCreateView,
    MainAdminView,
    student_payment_page,
    student_payment_view,
)

urlpatterns = [
    # Admin Page
    path("", MainAdminView.as_view(), name="admin_view"),

    # CRUD студентов
    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/create/", StudentCreateView.as_view(), name="create_student"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),

    # Оплата студента
    path("student/<int:pk>/payment_page/", student_payment_page, name="student_payment_page"),  
    path("student/<int:pk>/payment/", student_payment_view, name="student_payment"),           

    # Создание группы и тега
    path("groups/create/", GroupCreateView.as_view(), name="create_group"),
    path("tags/create/", TagCreateView.as_view(), name="create_tag"),
]
