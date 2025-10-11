from django import forms
from students.models import Student, Group, Tag


class StudentForm(forms.Form):
    name = forms.CharField(
        label="Имя студента", widget=forms.TextInput(attrs={"class": "student_input"})
    )
    surname = forms.CharField(
        label="Фамилия студента",
        widget=forms.TextInput(attrs={"class": "student_input"}),
    )
    age = forms.IntegerField(
        label="Возраст студента",
        widget=forms.TextInput(attrs={"class": "student_input"}),
    )
    number = forms.IntegerField(
        label="Номер футболиста",
        required=False,
        widget=forms.TextInput(attrs={"class": "student_input"}),
    )
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.TextInput(attrs={"class": "student_input"}),
    )
    phone_number = forms.CharField(
        label="Номер телефона", widget=forms.TextInput(attrs={"class": "student_input"})
    )
    group = forms.ModelChoiceField(label="Группа", queryset=Group.objects.all())
    description = forms.CharField(
        label="Комментарий",
        required=False,
        widget=forms.Textarea(attrs={"class": "student_input", "rows": 3}),
    )
    avatar = forms.ImageField(
        label="Аватарка",
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "student_input"}),
    )
    is_active = forms.BooleanField(label="Активен", required=False)
    tags = forms.ModelMultipleChoiceField(
        label="Теги",
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"class": "student_input"}),
    )


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
            "avatar": forms.ClearableFileInput(attrs={"class": "student_input"}),
            "description": forms.Textarea(attrs={"class": "student_input", "rows": 3}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "student_input"}),
            
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]
        labels = {"name": "Название группы"}
        widgets = {
            "name": forms.TextInput(attrs={"class": "student_input"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        labels = {"name": "Название тега"}
        widgets = {
            "name": forms.TextInput(attrs={"class": "student_input"}),
        }
