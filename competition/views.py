from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    competition = Competition.get_comptition(request)
    context = {
        "competition": competition,
    }

    return render(request, 'competition/index.html', context)
