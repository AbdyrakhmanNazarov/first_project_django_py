from django.apps import AppConfig

class StudentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "students"
    verbose_name = "Реал Мадрид"

    def ready(self):
        from . import signals
        return super().ready()    



