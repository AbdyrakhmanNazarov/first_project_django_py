from django import forms

class UserFilterForm(forms.Form):
    username = forms.CharField(required=False, label="Username")
    email = forms.CharField(required=False, label="Email")
