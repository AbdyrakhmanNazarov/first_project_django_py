from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),       # Главная/студенты
    path("accounts/", include("accounts.urls")),  # Логин/регистрация
    path("news/", include("news.urls")),          # Новости
    path("ckeditor/", include("ckeditor_uploader.urls")),  # CKEditor
    path("custom-admin/", include(("custom_admin.urls", "custom_admin"), namespace="custom_admin")),
    path("users/", include(("users.urls", "users"), namespace="users")),  # лайки, корзина, user page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
