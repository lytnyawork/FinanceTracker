from django.contrib import admin
from django.urls import include, path

from main.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = 'home'),
]
