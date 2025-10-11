from django.contrib import admin
from .models import Student, Group, Coach, Tag


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ("join_date", "updated_date")
    list_display = (
        "id",
        "name",
        "surname",
        "phone_number",
        "email",
        "number",
        "avatar_preview",
    )
    list_display_links = ("id", "name", "surname")
    search_fields = ("name", "surname", "group__name")
    list_filter = ("group__name", "age", "is_active", "tags")
    ordering = ("-join_date", "-updated_date")
    list_editable = ("phone_number", "email", "number")
    list_per_page = 5
    date_hierarchy = "join_date"
    filter_horizontal = ("tags",)

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "name",
                    "surname",
                    "age",
                    "number",
                    "phone_number",
                    "group",
                    "email",
                    "description",
                    "is_active",
                    "tags",
                )
            },
        ),
        (
            "Дополнительная информация",
            {"fields": ("join_date", "updated_date"), "classes": ("collapse",)},
        ),
    )

    save_on_top = True

    @admin.action(description="Активировать пользователя")
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=True)

    actions = [make_active]


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    readonly_fields = ("join_date", "updated_date")
    list_display = ("id", "name", "surname", "email", "phone_number", "avatar_preview")
    list_display_links = ("id", "name", "surname")
    search_fields = ("name", "surname")
    list_filter = ("age", "is_active")
    list_editable = ("phone_number", "email")
    list_per_page = 5
    ordering = ("-join_date", "-updated_date")
    save_on_top = True

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "name",
                    "surname",
                    "age",
                    "phone_number",
                    "group",
                    "email",
                    "description",
                    "is_active",
                )
            },
        ),
        (
            "Дополнительная информация",
            {"fields": ("join_date", "updated_date"), "classes": ("collapse",)},
        ),
    )

    @admin.action(description="Активировать пользователя")
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=True)

    actions = [make_active]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
