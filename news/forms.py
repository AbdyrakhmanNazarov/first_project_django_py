from django import forms
from news.models import News, NewsCategory

class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            "title",
            "subtitle",
            "content",
            "category",
            "image",
            "is_active",
        )
        labels = {
            "title":"Название темы",
            "subtitle":"Заголовок",
            "content":"Тема",
            "category":"Категория",
            "image":"Изображение",
            "is_active":"Активный",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "student_input"}),
            "subtitle": forms.TextInput(attrs={"class": "student_input"}),
            "content": forms.Textarea(attrs={"class": "student_input"}),
            "category": forms.Select(attrs={"class": "student_input"}),
            "image": forms.ClearableFileInput(attrs={"class": "student_input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "student_input"}),
        }


class NewsCategoryModelForm(forms.ModelForm):
    class Meta:
        model = NewsCategory
        fields = (
            "name",
        )
        labels = {
            "name":"Название категории",
        }
        widgets = {
           "name": forms.TextInput(attrs={"class": "student_input"}),
        }
