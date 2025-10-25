from django import forms
from students.models import Student, Group, Tag, StudentContract


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "name",
            "surname",
            "age",
            "number",
            "email",
            "phone_number",
            "group",
            "description",
            "avatar",
            "is_active",
            "tags",
        )
        labels = {
            "name": "Имя студента",
            "surname": "Фамилия студента",
            "age": "Возраст студента",
            "number": "Номер футболиста",
            "email": "Электронная почта",
            "phone_number": "Номер телефона",
            "group": "Группа",
            "description": "Комментарий",
            "avatar": "Аватарка",
            "is_active": "Активен",
            "tags": "Теги",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "student_input"}),
            "surname": forms.TextInput(attrs={"class": "student_input"}),
            "age": forms.NumberInput(attrs={"class": "student_input"}),
            "number": forms.NumberInput(attrs={"class": "student_input"}),
            "email": forms.EmailInput(attrs={"class": "student_input"}),
            "phone_number": forms.TextInput(attrs={"class": "student_input"}),
            "group": forms.Select(attrs={"class": "student_input"}),
            "description": forms.Textarea(attrs={"class": "student_input", "rows": 3}),
            "avatar": forms.ClearableFileInput(attrs={"class": "student_input"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "student_input"}),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]
        labels = {"name": "Название группы"}
        widgets = {"name": forms.TextInput(attrs={"class": "student_input"})}


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        labels = {"name": "Название тега"}
        widgets = {"name": forms.TextInput(attrs={"class": "student_input"})}


class PaymentForm(forms.ModelForm):
    amount = forms.DecimalField(
        label="Сумма оплаты (сом)",
        max_digits=10,
        decimal_places=2,
        initial=8000,
        widget=forms.NumberInput(attrs={"class": "student_input"}),
    )

    class Meta:
        model = StudentContract
        fields = ["amount"]

    def save(self, commit=True):
        contract = self.instance
        amount = self.cleaned_data["amount"]
        contract.make_payment(amount)
        return contract
