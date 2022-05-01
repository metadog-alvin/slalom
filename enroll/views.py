import random

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from player.models import Player
from .models import getEnroll
from pprint import pprint


def index(request):
    enrolls = getEnroll()
    context = {
        "enrolls": enrolls,
    }
    return render(request, 'enroll/index.html', context)


def apply(request):
    # return HttpResponse(random.randint(1,10))
    return render(request, 'enroll/apply.html')


def store(request):
    request.POST.get('player-id')
    request.POST.get('name')
    request.POST.get('identity')
    request.POST.get('gender')

    request.POST.get('agency')
    request.POST.get('leader')
    request.POST.get('coach')
    request.POST.get('manager')
    request.POST.get('director')

    request.POST.get('group-free-style')
    request.POST.get('level-free-style')
    request.POST.get('item-free-style[]')

    request.POST.get('group-speed')
    request.POST.get('level-speed')
    request.POST.get('item-speed[]')

    request.POST.get('level-d1ance')
    request.POST.get('item-dance[]')

    obj, created = Player.objects.update_or_create(
        id=request.POST.get('player-id'),
        defaults={
            'identity': request.POST.get('identity'),
            'name': request.POST.get('name'),
            'gender': request.POST.get('gender'),
            'city': request.POST.get('city'),
            'agency': request.POST.get('agency'),
            'created_by': 1,
        },
    )


    # getPlayerNumber()


    # try {
    # DB::
    # beginTransaction();
    #
    # $playerId = app(PlayerModel::class )->updateOrCreate(['id' = > $playerId], [
    # 'account_id' = > auth()->user()->id,
    # 'name'       = > $name,
    # 'gender'     = > $gender,
    # 'city'       = > $city,
    # 'agency'     = > $agency,
    # ])->id;
    #
    # $this->enrollModel->cancel($playerId);
    #
    # $playerNumber = $this->getPlayerNumber($playerId);
    #
    # if ($enrollItem) {
    #
    # foreach($enrollItem as $item) {
    # EnrollModel:: create([
    # 'game_id' = > config('app.game_id'),
    # 'player_id' = > $playerId,
    # 'player_number' = > $playerNumber,
    # 'account_id' = > auth()->user()->id,
    # 'city' = > $city,
    # 'agency' = > $agency,
    # 'level' = > $level,
    # 'group' = > $group,
    # 'gender' = > $gender,
    # 'item' = > $item,
    # 'coach' = > $coach,
    # 'leader' = > $leader,
    # 'manager' = > $manager,
    # 'director' = > $director,
    # ]);
    # }
    # }
    #
    # if ($flowerItem == '中級指定套路' & & $request->hasFile('soundFile')) {
    # $soundName = $this->getFlowerGroup($group).'-'. $flowerItem.
    # '-'. $name.
    # '.mp3';
    # Storage::put('flower_sound/'. $soundName, $request->file('soundFile')->get());
    # EnrollModel::create([
    # 'game_id' = > config('app.game_id'),
    # 'player_id' = > $playerId,
    # 'player_number' = > $playerNumber,
    # 'account_id' = > auth()->user()->id,
    # 'city' = > $city,
    # 'agency' = > $agency,
    # 'group' = > $group,
    # 'group2' = > $this->getFlowerGroup($group),
    # 'item' = > $flowerItem,
    # 'gender' = > $gender,
    # 'sound' = > $soundName,
    # ]);
    # }
    #
    # if ($flowerItem == '初級指定套路') {
    # EnrollModel::create([
    # 'game_id' = > config('app.game_id'),
    # 'player_id' = > $playerId,
    # 'player_number' = > $playerNumber,
    # 'account_id' = > auth()->user()->id,
    # 'city' = > $city,
    # 'agency' = > $agency,
    # 'group' = > $group,
    # 'group2' = > $this->getFlowerGroup($group),
    # 'item' = > $flowerItem,
    # 'gender' = > $gender,
    # 'sound' = > $sound == null ? '未選曲目': $sound,
    # ]);
    # }
    #
    # app(RegistryFeeModel::
    #
    # class ):
    # :
    #
    # updateOrCreate(
    # ['game_id' = > config('app.game_id'), 'account_id' = > auth()->user()->id, 'player_id' = > $playerId],
    # ['game_id' = > config(
    # 'app.game_id'), 'account_id' = > auth()->user()->id, 'player_id' = > $playerId, 'fee' = > $this->calculationFee($enrollItem, $flowerItem)]
    # );
    #
    # $this->registryFeeService->calculationTotal(auth()->user()->id);
    #
    # DB::commit();
    # return true;
    # } catch(\Exception $e) {
    # DB::rollback();
    # return false;
    # }

    messages.success(request, '報名成功')

    return redirect('enroll.apply')
    # get_data = {}
    # for key, value in request.POST.lists():
    #     get_data[key] = value
    # # values = request.POST.items()
    # pprint(get_data)

    # pprint(dir(request.POST.items()))
    # pprint(list(values))

    # return HttpResponse(request.POST.iteritems())
    # return HttpResponse(1)


def dd(request):
    post_data = {}
    for key, value in request.POST.lists():
        post_data[key] = value

    pprint(post_data)

    return JsonResponse(post_data)
