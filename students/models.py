from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import mark_safe
from django.utils import timezone
from datetime import timedelta


class Group(models.Model):
    name = models.CharField(max_length=100, default="Без имени")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Student(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Имя футболиста")
    surname = models.CharField(max_length=50, null=True, blank=True, verbose_name="Фамилия футболиста")
    age = models.IntegerField(null=True, blank=True, verbose_name="Возраст футболиста")
    number = models.IntegerField(null=True, blank=True, verbose_name="Номер футболиста")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почта")
    description = models.TextField(max_length=150, null=True, blank=True, verbose_name="Комментарий")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Группа")
    phone_number = PhoneNumberField(region="KG", default="+996000000000", verbose_name="Телефон")
    avatar = models.ImageField(upload_to="Фото_футболистов", null=True, blank=True)
    join_date = models.DateField(auto_now_add=False, editable=True, verbose_name="Дата присоединения") 
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    tags = models.ManyToManyField(Tag, related_name="students", blank=True)

    def __str__(self):
        return f"{self.surname or ''} {self.name or ''} - {self.age or ''}"

    class Meta:
        verbose_name = "Футболист"
        verbose_name_plural = "Футболисты"

    def avatar_preview(self):
        if self.avatar:
            return mark_safe(f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:5px"/>')
        return "—"
    avatar_preview.short_description = "Аватарка"

    def get_balance(self):
        if hasattr(self, 'contract') and self.contract:
            return self.contract.balance
        return 0

    def get_group_name(self):
        return self.group.name if self.group else "Без группы"


class Coach(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Имя тренера")
    surname = models.CharField(max_length=50, null=True, blank=True, verbose_name="Фамилия тренера")
    age = models.IntegerField(default=12, verbose_name="Возраст тренера")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почта")
    description = models.TextField(max_length=150, null=True, blank=True, verbose_name="Комментарий")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Группа")
    phone_number = PhoneNumberField(region="KG", default="+996000000000", verbose_name="Телефон")
    avatar = models.ImageField(upload_to="Фото_тренеров", null=True, blank=True)
    join_date = models.DateField(auto_now_add=True, verbose_name="Дата присоединения")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.surname or ''} {self.name or ''}"

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def avatar_preview(self):
        if self.avatar:
            return mark_safe(f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:5px"/>')
        return "—"
    avatar_preview.short_description = "Аватарка"


class StudentContract(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="contract")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Баланс")
    last_payment_date = models.DateField(default=timezone.now, verbose_name="Последняя дата оплаты")

    MONTHLY_FEE = 8000  # фиксированная ежемесячная сумма

    def __str__(self):
        student_name = f"{self.student.surname or ''} {self.student.name or ''}"
        return f"Контракт для {student_name}, баланс: {self.balance}"

    class Meta:
        verbose_name = "Контракт студента"
        verbose_name_plural = "Контракты студентов"

    def deduct_monthly_fee(self):
        today = timezone.now().date()
        if (today - self.last_payment_date) >= timedelta(days=30):
            self.balance -= self.MONTHLY_FEE
            self.last_payment_date = today
            self.save()

    def make_payment(self, amount):
        self.balance += amount
        self.save()

    def reset_balance(self):
        self.balance = 0
        self.last_payment_date = timezone.now().date()
        self.save()
