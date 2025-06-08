from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from userprofile.forms import BillForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'main/index.html'

        
class StepView(LoginRequiredMixin,CreateView):
    template_name = 'main/step1.html'
    form_class = BillForm
    


               