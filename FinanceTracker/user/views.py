from django.shortcuts import render
from django.contrib.auth.views import LoginView

from user.forms import LoginUserForm

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/auth.html'
    