from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('translator/',views.translator, name='translator'),
    path('translated/',views.translated, name='translated')
    
]