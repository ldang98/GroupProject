from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from django.http import HttpResponse


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'account.html')
        else:
            messages.info(request, 'Invalid Credentials.')
            return redirect('/')

    else:
        return render(request, 'account.html')


def home(request):
    return render(request, 'home.html')