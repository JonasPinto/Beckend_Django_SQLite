from django.urls import path
from django import index, contato

urlpatterns = [
    path('', index),
    path('contato', contato),
]