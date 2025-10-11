"""
URL configuration for less_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from students.views import (
    main,
    student_detail,
    create_student,
    student_update,
    delete_student,
    create_tag,
    create_group,
)

urlpatterns = [
    path("", main, name="main"),
    path("admin/", admin.site.urls),
    path("student-create/", create_student, name="create_student"),
    path("students/<int:id>/", student_detail, name="student_detail"),
    path("students/<int:id>/update", student_update, name="student_update"),
    path("students/<int:id>/delete", delete_student, name="delete_student"),
    path("create-group/", create_group, name="create_group"),
    path("create-tag/", create_tag, name="create_tag"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
