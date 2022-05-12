from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

enroll = [
    path('', login_required(views.index), name='enroll'),

    path('cancel/', login_required(views.cancel), name='enroll.cancel'),
    path('apply/<int:player_id>', login_required(views.apply), name='enroll.apply'),
    path('apply', login_required(views.apply), name='enroll.apply'),

    path('store/', login_required(views.store), name='enroll.store'),
]