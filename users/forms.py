from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

class RegistrationForm(UserCreationForm):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )
    STUDENT = 1
    WORKER = 2
    PRESIDENT = 3
    MILITARY = 4
    POS_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("PRESIDENT", "PRESIDENT"),
        ("MILITARY", "MILITARY")
    )
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    position = forms.ChoiceField(choices=POS_CHOICE, required=True)
    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "age",
            "gender",
            "position",
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "type password",
                "id": "password"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "email",
                "id": "email"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "type password",
                "id": "password"
            }
        )
    )

