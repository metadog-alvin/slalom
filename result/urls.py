from django.urls import path
from . import views

result = [
    path('', views.index, name='result'),
]
