from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path("", views.Index,  name="Index"),
    path("suggest_output/", views.suggest_output, name="suggest_output"),
]
