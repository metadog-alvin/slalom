from django.core import serializers
from collections.abc import Iterable
from django.db.models.query import QuerySet


def dd(request):
    get_data = {}
    for key, value in request.GET.lists():
        get_data[key] = value

    post_data = {}
    for key, value in request.POST.lists():
        post_data[key] = value

    files = {}
    for key, value in request.FILES.lists():
        files['name'] = request.FILES[key].name
        files['content_type'] = request.FILES[key].content_type
        files['size'] = request.FILES[key].size

