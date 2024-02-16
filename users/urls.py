from django.urls import path
from django.contrib.auth import login
from .import views

urlpatterns = [
    path("users/", views.login, name='login'),
]
