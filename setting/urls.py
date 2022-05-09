from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

setting = [
    path('', login_required(views.index), name='setting'),
]