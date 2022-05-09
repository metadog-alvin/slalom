from django.urls import path
from . import views

competition = [
    path('', views.index, name='competition'),
]
