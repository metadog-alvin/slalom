from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return redirect('enroll');
    # return render(request, 'sidebar.html')


# def confucianism_detail(request):
#     return HttpResponse("Confucianism 是儒家的英文")