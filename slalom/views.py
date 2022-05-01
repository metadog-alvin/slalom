from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html')

    def post(self, request, *args, **kwargs):
        print(request.POST.get('account'))
        print(request.POST.get('password'))

        user = authenticate(request, account=request.POST['account'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse('login success')

        return HttpResponse('login failed')
        # return redirect('enroll')
#
def index(request):
    # return HttpResponse('111')
    return redirect('enroll')
    # return render(request, 'sidebar.html')
#
# class user_login(View):
#
#     def get(request):
#         return HttpResponse('get')
#
#     def post(request):
#         return HttpResponse('post')
#         user = authenticate(request, account=request.POST['account'], password=request.POST['password'])
#         if user is not None:
#             login(request, user)
#             return HttpResponse('login success')
#
#         return HttpResponse('login failed')

    # return render(request, 'auth/login.html')
