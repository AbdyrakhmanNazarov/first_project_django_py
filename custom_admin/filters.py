# filters.py
import django_filters
from django.contrib.auth.models import User
from django import forms
from students.models import Student


class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Имя"
    )
    group = django_filters.CharFilter(
        field_name="group__name", lookup_expr="icontains", label="Группа"
    )
    join_date = django_filters.DateFromToRangeFilter(label="Дата поступления")

    class Meta:
        model = Student
        fields = ["name", "group", "join_date"]

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"placeholder": "Введите имя"})
    )
    email = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Введите email"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "is_active"]
