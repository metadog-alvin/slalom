from django.http import HttpResponse
from django.shortcuts import render
from .models import Enroll, getEnroll


def index(request):
    enrolls = getEnroll()
    context = {
        "enrolls": enrolls,
    }
    return render(request, 'enroll/index.html', context)
