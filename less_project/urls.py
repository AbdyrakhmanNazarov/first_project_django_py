from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),            
    path("accounts/", include("accounts.urls")),   
    path("custom-admin/", include("custom_admin.urls")),  
    path("news/", include("news.urls")),           
    path("ckeditor/", include("ckeditor_uploader.urls")),  
    path('users/', include('users.urls')),
]

# Static & Media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)