from django.contrib import admin
from django.urls import include, path
from . import views

from user.views import LoginUser


app_name='users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name = 'auth'),
    path('logout/', views.logout_user, name='logout'),
]