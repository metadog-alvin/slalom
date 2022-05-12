from pprint import pprint

from django.contrib import messages

from django.shortcuts import render, redirect
from competition.models import Competition


def index(request):
    return render(request, 'admin/setting/index.html')


def store(request):
    Competition.objects.create(
        name=request.POST.get('name'),
        letter=request.POST.get('letter'),
        date=request.POST.get('date'),
        start_time=request.POST.get('start_time'),
        is_open_document=request.POST.get('is_open_document'),
        is_open_enroll=request.POST.get('is_open_enroll'),
        is_open_estimate=request.POST.get('is_open_estimate'),
        created_by=request.user.id
    )

    messages.success(request, '設定成功')

    return redirect('setting')
