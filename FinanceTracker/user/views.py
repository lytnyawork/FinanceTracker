from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView
from django.views.generic.edit import CreateView


from user.forms import LoginUserForm, RegisterUserForm




class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = "user/login.html"
    

    def form_valid(self, form):
        remember_me = form.cleaned_data.get("remember_me")

        

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super().form_valid(form)

class CreateUserView(CreateView):
    form_class= RegisterUserForm
    template_name = "user/register.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        
        user = form.save()
        login(self.request, user)
        return redirect('home')

    


def logout_user(request) -> HttpResponseRedirect:
    print(request.method)
    logout(request)
    return HttpResponseRedirect(reverse("home"))
