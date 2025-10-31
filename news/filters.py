import django_filters
from django import forms
from .models import News, NewsCategory


class NewsFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=NewsCategory.objects.all(),
        label="Категория",
        empty_label="Выбрать категорию",
        widget=forms.Select(attrs={"class": "student_input"}),
        required=False,
    )

    class Meta:
        model = News
        fields = ("category",)
