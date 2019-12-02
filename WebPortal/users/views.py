from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')


# def account(request):
#     return render(request, 'account.html')


