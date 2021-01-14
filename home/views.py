from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required(login_url='/auth/login/')

def home(request):
    list_login = User.objects.all()
    if request.method == "POST":
        return render(request, 'home.html')

    else:

        return render(request, 'home.html',
                      {"list_login": list_login})
