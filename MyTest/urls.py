from django.contrib import admin
from django.urls import path

from MyTest import views

urlpatterns = [
   path('index', views.index)
]