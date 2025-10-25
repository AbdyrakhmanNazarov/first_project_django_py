from django.views.generic import TemplateView
from django.core.paginator import Paginator
from students.models import Student
from students.filters import StudentFilter


# ===============================
# Главная страница (открыта для всех)
# ===============================
class MainTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filterset = StudentFilter(self.request.GET, queryset=Student.objects.all())
        students_list = filterset.qs

        paginator = Paginator(students_list, 3)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context.update(
            {
                "students": page_obj,
                "page_obj": page_obj,
                "paginator": paginator,
                "is_paginated": page_obj.has_other_pages(),
                "filter": filterset,
                "title": "Главная страница",
            }
        )
        return context


# ===============================
# About страница
# ===============================
class AboutTemplateView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Page"
        return context


# ===============================
# Contacts страница
# ===============================
class ContactsTemplateView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contacts Page"
        return context
