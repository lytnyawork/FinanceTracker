from django.contrib import admin
from django.urls import include, path
from . import views

from user.views import CreateUserView, LoginUserView


app_name='users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name = 'login'),
    path('register/', CreateUserView.as_view(), name= 'register'),
    path('logout/', views.logout_user, name='logout'),
]