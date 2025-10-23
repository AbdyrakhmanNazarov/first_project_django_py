from django.contrib import admin
from .models import Student, Group, Coach, Tag, StudentContract


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ("join_date", "updated_date", "avatar_preview")
    list_display = (
        "id",
        "name",
        "surname",
        "phone_number",
        "email",
        "number",
        "get_group_name",
        "get_balance",
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

    @admin.action(description="Активировать выбранных студентов")
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=True)

    actions = [make_active]

    def get_balance(self, obj):
        return obj.get_balance()
    get_balance.short_description = "Баланс"

    def get_group_name(self, obj):
        return obj.get_group_name()
    get_group_name.short_description = "Группа"


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    readonly_fields = ("join_date", "updated_date", "avatar_preview")
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

    @admin.action(description="Активировать выбранных тренеров")
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


@admin.register(StudentContract)
class StudentContractAdmin(admin.ModelAdmin):
    list_display = ("id", "get_student_name", "balance")
    search_fields = ("student__name", "student__surname")

    def get_student_name(self, obj):
        return str(obj.student)
    get_student_name.short_description = "Студент"
