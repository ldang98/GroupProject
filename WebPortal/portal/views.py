from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group, Permission

from django.http import HttpResponse


# Son's Code
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user) #have code here that decides which page to go to based on group 
            if user.groups.filter(name='Global').exists():
                return render(request, 'Global.html')
            if user.groups.filter(name='Finance').exists():
                return render(request, 'account.html')
            if user.groups.filter(name='Sales').exists():
                return render(request, 'SalesTemplate.html')
            if user.groups.filter(name='HR').exists():
                return render(request, 'HRTemplate.html')
            if user.groups.filter(name='Engineering').exists():
                return render(request, 'EngineeringTemplate.html')
        else:
            messages.info(request, 'Invalid Credentials.')
            return redirect('/')
    else:
        return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')

