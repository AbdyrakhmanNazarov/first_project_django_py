from django.urls import path
from .views import (
    MainTemplateView,
    AboutTemplateView,
    ContactsTemplateView,
    toggle_like,
    add_to_cart,
    cart_view,
    clear_cart,
)

urlpatterns = [
    # Главная и информационные страницы
    path('', MainTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),

    # Лайки студентов
    path('like/<int:student_id>/', toggle_like, name='toggle_like'),

    #  Корзина студентов
    path('cart/add/<int:student_id>/', add_to_cart, name='add_to_cart'), 
    path('cart/', cart_view, name='cart_view'),                             
    path('cart/clear/', clear_cart, name='clear_cart'),                     
]
