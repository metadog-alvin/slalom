from django.http import HttpResponse
from django.urls import path, include


from competition.urls import competition
from doc.urls import doc
from result.urls import result
from enroll.urls import enroll
from schedule.urls import schedule
from setting.urls import setting
from user.urls import user
from . import views
from .views import SignIn, SignUp

urlpatterns = [
    # client
    path('', views.index, name='index'),
    path('sign-in', SignIn.as_view(), name='sign-in'),
    path('sign-up', SignUp.as_view(), name='sign-up'),
    path('sign-out', views.sign_out, name='sign-out'),
    path('enroll/', include(enroll)),
    path('competition/', include(competition)),
    path('result', include(result)),
    path('schedule', include(schedule)),
    path('doc', include(doc)),

    # manager
    path('setting', include(setting)),

    # admin
    path('user', include(user)),
    # path('credit/', include(enroll)),
    # path('fee', include('fee.urls')),
    # path('payment', include('payment.urls')),

    # path('player', include('player.urls')),
    # path('admin/', admin.site.urls),
]
