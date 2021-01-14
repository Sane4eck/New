from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


@login_required
def user_logout(request):
    auth.logout(request)
    return redirect('/auth/login/')


def login(request):
    if request.method == 'POST':
        data = request.POST
        login_1 = data['login']
        password_1 = data['password']
        user = auth.authenticate(username=login_1, password=password_1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse('не туда попал')
    else:
        return render(request, 'login.html')


def user_register(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        email = data['email']
        password_again = data['password_again']
        if password == password_again:
            user_ = User.objects.create_user(username=username,
                                             password=password,
                                             email=email)

            user_.save()
            return redirect('/')
        else:
            redirect('/auth/login')
    else:
        return render(request, 'register.html')
