from pprint import pprint

from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.base_user import BaseUserManager
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from user.models import User


class SignIn(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/sign-in.html')

    def post(self, request, *args, **kwargs):
        account = request.POST.get('account')
        password = request.POST.get('password')

        user = User.objects.get(account=account)
        if user.check_password(password):
            login(request, user)

            if user.is_active is True :
                messages.success(request, 'Sign-In Success')

                if request.POST.get('next') != '':
                    return redirect(request.POST.get('next'))
                return redirect('enroll')

            pprint(user.account + 'Sign In Fail')
            return redirect('sign-in')

        return HttpResponse('login fail')

class SignUp(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/sign-up.html')

    def post(self, request, *args, **kwargs):

        user = User()
        user.account = request.POST.get('account')
        user.full_name = request.POST.get('full_name')
        user.team_name = request.POST.get('team_name')
        user.set_password(request.POST.get('password'))
        user.save()

        login(request, user)

        messages.success(request, 'Register Success')

        return redirect('enroll')

        # User.objects.create(account=request.POST.get('account'), password=request.POST.get('password'))

        # return HttpResponse('sign-up success')
        # return redirect('enroll')


def sign_out(request):
    auth.logout(request)

    return redirect('index')


def index(request):
    # return HttpResponse('111')
    # return redirect('enroll')
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


# 參考
# /Library/Python/3.8/site-packages/django/contrib/auth/base_user.py