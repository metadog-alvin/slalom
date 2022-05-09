from django.urls import path
from . import views

schedule = [
    path('', views.index, name='schedule'),
]