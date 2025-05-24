from django.contrib import admin
from django.urls import include, path

from user.views import LoginUser

urlpatterns = [
    path('login/', LoginUser.as_view(), name = 'auth'),
]