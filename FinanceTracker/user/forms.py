from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError, widgets


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="Запомнить меня",
    )

    username.widget.attrs.update({"class": "form-control", "placeholder": "Логин"})
    password.widget.attrs.update({"class": "form-control", "placeholder": "Пароль"})

    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    username = username = forms.CharField(label="Логин")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повторение пароля", widget=forms.PasswordInput())

    username.widget.attrs.update({"class": "form-control", "placeholder": "Логин"})
    email.widget.attrs.update({"class": "form-control", "placeholder": "Email"})
    password1.widget.attrs.update({"class": "form-control", "placeholder": "Пароль"})
    password2.widget.attrs.update({"class": "form-control", "placeholder": "Повторение пароля"})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот email уже используется")
        return email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
