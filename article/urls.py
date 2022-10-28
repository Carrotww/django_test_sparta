from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", view=views.ArticleView.as_view(), name='article_view'),
]