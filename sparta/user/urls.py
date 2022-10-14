from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.sign_up, name='sign_up'),
    path("login/", views.login, name='login'),
    path("home/", views.home, name='home'),
]
