from django.urls import path
from . import views

doc = [
    path('doc/group', views.group, name='doc.group'),
    path('doc/agency', views.agency, name='doc.agency'),
]