from django.contrib import admin
from django.urls import include, path

from main.views import IndexView, StepView

urlpatterns = [
    path('', IndexView.as_view(), name = 'home'),
    path('step1', StepView.as_view(), name = 'step'),
]
