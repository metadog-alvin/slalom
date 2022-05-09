from django.shortcuts import render

def group(request):
    return render(request, 'doc/group.html')

def agency(request):
    return render(request, 'doc/agency.html')

