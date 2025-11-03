from django.urls import path
from .views import user_page, toggle_like, add_to_cart, cart_view, clear_cart, liked_students_view

app_name = "users"

urlpatterns = [
    path("page/", user_page, name="user_page"),
    path("student/<int:student_id>/like/", toggle_like, name="like_student"),
    path("student/<int:student_id>/add_to_cart/", add_to_cart, name="add_to_cart"),
    path("cart/", cart_view, name="cart_view"),
    path("cart/clear/", clear_cart, name="clear_cart"),
    path("liked-students/", liked_students_view, name="liked_students"),
]
