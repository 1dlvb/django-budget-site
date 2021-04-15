from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^about', views.about, name='about'),
    re_path(r'^login', views.login, name='login'),

]
