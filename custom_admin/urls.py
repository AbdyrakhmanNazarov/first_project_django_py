from django.urls import path
from custom_admin.views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    GroupCreateView,
    TagCreateView,
    MainAdminView,
    student_payment_page,
    student_payment_view,
    set_cookie_view,
    get_cookie_view,
    set_session_view,
    get_session_view,
    visit_counter,
    delete_cookie_view,
    delete_session_view,
    toggle_like,      
    add_to_cart,
    clear_cart,
)

urlpatterns = [
    # Admin Page
    path("", MainAdminView.as_view(), name="admin_view"),
    
    # CRUD студентов
    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/create/", StudentCreateView.as_view(), name="create_student"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),

    # Оплата студента
    path("student/<int:pk>/payment_page/", student_payment_page, name="student_payment_page"),
    path("student/<int:pk>/payment/", student_payment_view, name="student_payment"),

    # Создание группы и тега
    path("groups/create/", GroupCreateView.as_view(), name="create_group"),
    path("tags/create/", TagCreateView.as_view(), name="create_tag"),

    # Куки
    path("set-cookie-test/", set_cookie_view, name="set_cookie_test"),
    path("get-cookie-test/", get_cookie_view, name="get_cookie_test"),
    path("del-cookie/", delete_cookie_view, name="delete_cookie"),

    # Сессии
    path("set-session/", set_session_view, name="set_session"),
    path("get-session/", get_session_view, name="get_session"),
    path("visit-counter-page/", visit_counter, name="visit_counter"),
    path("del-session/", delete_session_view, name="delete_session"),

    # ❤️ Лайки
    path("student/<int:student_id>/like/", toggle_like, name="like_student"),

    # 🛒 Корзина
    path("student/<int:student_id>/add_to_cart/", add_to_cart, name="add_to_cart"),
    path("cart/clear/", clear_cart, name="clear_cart"),
]
