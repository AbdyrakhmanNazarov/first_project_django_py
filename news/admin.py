from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import NewsCategory, News

# Настройки заголовка админки
admin.site.site_header = "Админ-панель сайта Реал Мадрид"
admin.site.site_title = "Real Madrid Admin"


# ============================= #
# Админка для категорий новостей #
# ============================= #
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


# ============================= #
# Форма для News с CKEditor      #
# ============================= #
class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            "content": CKEditorUploadingWidget(),
        }


# ============================= #
# Админка для новостей           #
# ============================= #
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "subtitle", "created_at", "category", "is_active")
    search_fields = ("title", "subtitle", "content")
    list_filter = ("created_at", "category", "is_active")
    form = NewsAdminForm


# ============================= #
# Регистрация в админке          #
# ============================= #
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(News, NewsAdmin)
