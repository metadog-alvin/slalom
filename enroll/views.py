import random

from django.contrib import messages

from django.db.models import Max, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db import transaction
from MySQLdb import IntegrityError

from player.models import Player
from .models import Enroll
from pprint import pprint


def index(request):
    request.session['competition'] = 21

    enrolls = Enroll.objects.filter(competition_id=request.session['competition'], user_id=request.user.id).values('agency', 'user_id', 'competition_id', 'player__name','player_id').annotate(count=Count('player_id'))

    print(enrolls.query)
    for enroll in enrolls:
        enroll['item'] = Enroll.objects.filter(competition_id=request.session['competition'], user_id=request.user.id, player_id=enroll['player_id'])
        print(enroll['agency'])

    context = {
        "enrolls": enrolls,
    }

    return render(request, 'enroll/index.html', context)


def apply(request, player_id=0):
    player = None
    enrolls = None

    players = Player.objects.filter(created_by=request.user.id)

    if player_id is not 0:
        player = Player.objects.get(id=player_id)
        enrolls = Enroll.objects.filter(player_id=player_id, competition_id=request.session['competition'])

    context = {
        'player_id': player_id,
        'enrolls': enrolls,
        'player': player,
        'players': players,
    }
    return render(request, 'enroll/apply.html', context)


def store(request):
    try:
        with transaction.atomic():
            create_or_update_player(request)
            player_number = get_player_number(request)
            delete_enroll(request)
            enroll_free_style(request, player_number)
            enroll_speed(request, player_number)
            enroll_dance(request, player_number)

            messages.success(request, '報名成功')

            return redirect('enroll')
    except IntegrityError:
        return HttpResponse('fail')


def enroll_free_style(request, player_number):
    for free_style in request.POST.getlist('item_free_style[]'):
        Enroll.objects.update_or_create(
            competition_id=request.session['competition'],
            user_id=request.user.id,
            player_id=request.POST.get('player_id'),
            number=player_number,
            level=request.POST.get('level_free_style'),
            group=request.POST.get('group_free_style'),
            item=free_style,
            type='free_style',
            gender=request.POST.get('gender'),
            defaults={
                'agency': request.POST.get('agency'),
                'coach': request.POST.get('coach'),
                'leader': request.POST.get('leader'),
                'manager': request.POST.get('manager'),
                'director': request.POST.get('director'),
            },
        )


def enroll_speed(request, player_number):
    for speed in request.POST.getlist('item_speed[]'):
        Enroll.objects.update_or_create(
            competition_id=request.session['competition'],
            user_id=request.user.id,
            player_id=request.POST.get('player_id'),
            number=player_number,
            level=request.POST.get('level_speed'),
            group=request.POST.get('group_speed'),
            item=speed,
            type='speed',
            gender=request.POST.get('gender'),
            defaults={
                'agency': request.POST.get('agency'),
                'coach': request.POST.get('coach'),
                'leader': request.POST.get('leader'),
                'manager': request.POST.get('manager'),
                'director': request.POST.get('director'),
            },
        )


def enroll_dance(request, player_number):
    for dance in request.POST.getlist('item_dance[]'):
        Enroll.objects.update_or_create(
            competition_id=request.session['competition'],
            user_id=request.user.id,
            player_id=request.POST.get('player_id'),
            number=player_number,
            level=request.POST.get('level_dance'),
            item=dance,
            type='dance',
            gender=request.POST.get('gender'),
            defaults={
                'agency': request.POST.get('agency'),
                'coach': request.POST.get('coach'),
                'leader': request.POST.get('leader'),
                'manager': request.POST.get('manager'),
                'director': request.POST.get('director'),
            },
        )


def create_or_update_player(request):
    player_id = int(request.POST.get('player_id'))

    if player_id == '0':
        player = Player()
    else:
        player = Player.objects.get(id=player_id)

    player.identity = request.POST.get('identity')
    player.name = request.POST.get('name')
    player.gender = request.POST.get('gender')
    player.agency = request.POST.get('agency')
    player.created_by = request.user.id
    player.save()


def get_player_number(request):
    enroll = Enroll.objects.filter(
        competition_id=request.session['competition'],
        player_id=request.POST.get('player_id'),
    ).first()

    if enroll is None:
        maxNumber = Enroll.objects.filter(
            competition_id=request.session['competition'],
        ).aggregate(Max('number')).get('number__max')

        if maxNumber is None:
            playerNumber = 1
        else:
            playerNumber = maxNumber + 1
    else:
        playerNumber = enroll.number

    return playerNumber


def delete_enroll(request):
    Enroll.objects.filter(
        competition_id=request.session['competition'],
        player_id=request.POST.get('player_id'),
    ).delete()


def cancel(request):
    delete_enroll(request)
    messages.warning(request, '取消報名成功')

    return redirect('enroll')

from django.core import serializers
from collections.abc import Iterable
from django.db.models.query import QuerySet
from django.core.exceptions import ObjectDoesNotExist


def dd(request, data=''):
    try:
        scheme = request.scheme
        server_name = request.META['SERVER_NAME']
        server_port = request.META['SERVER_PORT']
        remote_addr = request.META['REMOTE_ADDR']
        user_agent = request.META['HTTP_USER_AGENT']
        path = request.path
        method = request.method
        session = request.session
        cookies = request.COOKIES

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

        dump_data = ''
        query_data = ''
        executed_query = ''
        if data:
            if isinstance(data, Iterable):
                if isinstance(data, QuerySet):
                    executed_query = data.query
                    query_data = serializers.serialize('json', data)
                else:
                    dump_data = dict(data)
            else:
                query_data = serializers.serialize('json', [data])

        msg = f'''
            <html>
                <span style="color: red;"><b>Scheme</b></span>        : <span style="color: blue;">{scheme}</span><br>
                <span style="color: red;"><b>Server Name</b></span>   : <span style="color: blue;">{server_name}</span><br>
                <span style="color: red;"><b>Server Port</b></span>   : <span style="color: blue;">{server_port}</span><br>
                <span style="color: red;"><b>Remote Address</b></span>: <span style="color: blue;">{remote_addr}</span><br>
                <span style="color: red;"><b>User Agent</b></span>    : <span style="color: blue;">{user_agent}</span><br>
                <span style="color: red;"><b>Path</b></span>          : <span style="color: blue;">{path}</span><br>
                <span style="color: red;"><b>Method</b></span>        : <span style="color: blue;">{method}</span><br>
                <span style="color: red;"><b>Session</b></span>       : <span style="color: blue;">{session}</span><br>
                <span style="color: red;"><b>Cookies</b></span>       : <span style="color: blue;">{cookies}</span><br>
                <span style="color: red;"><b>Get Data</b></span>      : <span style="color: blue;">{get_data}</span><br>
                <span style="color: red;"><b>Post Data</b></span>     : <span style="color: blue;">{post_data}</span><br>
                <span style="color: red;"><b>Files</b></span>         : <span style="color: blue;">{files}</span><br>
                <span style="color: red;"><b>Executed Query</b></span>: <span style="color: blue;"><br>{executed_query}</span><br>
                <span style="color: red;"><b>Query Data</b></span>    : <span style="color: blue;"><br>{query_data}</span><br>
                <span style="color: red;"><b>Dump Data</b></span>     : <span style="color: blue;"><br>{dump_data}</span><br>
            </html>
        '''

        return msg
    except ObjectDoesNotExist:
        return False


def jjson(data):
    qs_json = serializers.serialize('json', data)
    return HttpResponse(qs_json, content_type='application/json')


