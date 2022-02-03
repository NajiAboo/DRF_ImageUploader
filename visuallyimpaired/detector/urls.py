from re import template

from django.contrib import admin
from django.urls import path
 
from . import views

urlpatterns = [
    path('', views.index),
    path('detect', views.DetectView.as_view(), name="detect")
]
