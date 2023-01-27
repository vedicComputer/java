from django.contrib import admin
from django.urls import path
from java import views


urlpatterns = [
    path("",views.vedic,name='vedic'),
]