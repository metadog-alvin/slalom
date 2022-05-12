from django.shortcuts import render

from user.models import User


def index(request):
    context = {
        'users': User.objects.all(),
    }

    return render(request, 'admin/user/index.html', context)