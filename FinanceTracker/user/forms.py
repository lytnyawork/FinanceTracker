from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    username = forms.CharField( label = 'Логин')
    password = forms.CharField( label = 'Пароль')

    username.widget.attrs.update({"class": "form-control"})
    password.widget.attrs.update({"class": "form-control"})

    class Meta:
        model = User
        fields = ['username','password']