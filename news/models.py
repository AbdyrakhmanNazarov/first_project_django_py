from django.db import models
from django.utils.html import mark_safe

class NewsCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
class News(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="Тема блога")
    subtitle = models.CharField(max_length=50, null=True, blank=True, verbose_name="Заголовок")
    content = models.TextField(max_length=150, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    image = models.ImageField(upload_to="Картинки", null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.title or ''} {self.category or ''}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def avatar_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" style="border-radius:5px; object-fit:cover;"/>')
        return "—"
    avatar_preview.short_description = "Изображение"
