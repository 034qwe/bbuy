from django.contrib import admin
from django.urls import path,include
import views

urlpatterns = [
    path('main/',views.index,name='main'),
    ]
