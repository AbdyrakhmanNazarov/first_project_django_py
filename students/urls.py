from django.urls import path
from students.views import (
    MainTemplateView,
    AboutTemplateView,
    ContactsTemplateView,
)

urlpatterns = [
    # Главная About Contacts
    path("", MainTemplateView.as_view(), name="main"),
    path("about/", AboutTemplateView.as_view(), name="about"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
