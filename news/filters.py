import django_filters
from django import forms
from .models import News, NewsCategory

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Поиск по заголовку",
        widget=forms.TextInput(attrs={
            "placeholder": "Введите название...",
            "class": "form-control"
        })
    )

    category = django_filters.ModelChoiceFilter(
        queryset=NewsCategory.objects.all(),
        label="Категория",
        empty_label="Все категории",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = News
        fields = ["title", "category"]
