from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse

from user.forms import LoginUserForm

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/auth.html'

    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))