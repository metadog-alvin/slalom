from django.urls import path
from . import views

user = [
    path('', views.index, name='user'),
]
