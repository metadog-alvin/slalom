from django.shortcuts import render


def index(request):
    # competition = Competition.get_comptition(request)
    # context = {
    #     "competition": competition,
    # }

    return render(request, 'schedule/index.html')

