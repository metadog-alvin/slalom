from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.views import View

from enroll import views
from .views import Login

enroll = [
    path('', views.index, name='enroll'),
    path('apply/', views.apply, name='enroll.apply'),
    path('store/', views.store, name='enroll.store'),
]

from competition import views

competition = [
    path('', views.index, name='competition'),
]

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', Login.as_view(), name='login'),
    path('enroll/', include(enroll)),
    path('competition/', include(competition)),

    # path('admin/', admin.site.urls),
    # path('credit/', include(enroll)),
    # path('fee', include('fee.urls')),
    # path('payment', include('payment.urls')),
    # path('result', include('result.urls')),
    # path('schedule', include('schedule.urls')),
    # path('user', include('user.urls')),
    # path('player', include('player.urls')),

]

# urlpatterns = [
#     path('', main_views.homepage),
#     path('help/', include('apps.help.urls')),
#     path('credit/', include(extra_patterns)),
# ]
