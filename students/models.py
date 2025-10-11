from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import mark_safe


class Group(models.Model):
    name = models.CharField(max_length=100, default="Без имени")

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


# ------------------------------------------------------------------------


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


# ------------------------------------------------------------------------


class Student(models.Model):
    name = models.CharField(
        verbose_name="Имя футболиста", max_length=50, null=True, blank=True
    )
    surname = models.CharField(
        verbose_name="Фамилия футболиста", max_length=50, null=True, blank=True
    )
    age = models.IntegerField(verbose_name="Возраст футболиста", null=True, blank=True)
    number = models.IntegerField(verbose_name="Номер футболиста", null=True, blank=True)
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    description = models.TextField(
        verbose_name="Коментарий", max_length=150, null=True, blank=True
    )
    group = models.ForeignKey(
        "Group", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Группа"
    )
    phone_number = PhoneNumberField(
        verbose_name="Телефон", region="KG", default="+996000000000"
    )
    avatar = models.ImageField(upload_to="Фото_футболистов", null=True)
    join_date = models.DateField(verbose_name="Дата присоединения", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    tags = models.ManyToManyField(Tag, related_name="students")

    def __str__(self):
        return f"{self.surname} {self.name} - {self.age}"

    class Meta:
        verbose_name = "Футболист"
        verbose_name_plural = "Футболисты"

    def avatar_preview(self):
        if self.avatar:
            return mark_safe(
                f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:5px"/>'
            )
        return "—"

    avatar_preview.short_description = "Аватарка"


# ------------------------------------------------------------------------


class Coach(models.Model):
    name = models.CharField(
        verbose_name="Имя тренера", max_length=50, null=True, blank=True
    )
    surname = models.CharField(
        verbose_name="Фамилия тренера", max_length=50, null=True, blank=True
    )
    age = models.IntegerField(verbose_name="Возраст тренера", default=12)
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    description = models.TextField(
        verbose_name="Коментарий", max_length=150, null=True, blank=True
    )
    group = models.ForeignKey(
        "Group", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Группа"
    )
    phone_number = PhoneNumberField(
        verbose_name="Телефон", region="KG", default="+996000000000"
    )
    avatar = models.ImageField(upload_to="Фото_тренеров", null=True)
    join_date = models.DateField(verbose_name="Дата присоединения", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def avatar_preview(self):
        if self.avatar:
            return mark_safe(
                f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:5px"/>'
            )
        return "Нету аватара"

    avatar_preview.short_description = "Аватарка"


# ------------------------------------------------------------------------
