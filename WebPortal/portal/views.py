from itertools import chain
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group, Permission
from .models import Link
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def login(request):
    # if (request.method == 'POST'):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     user = auth.authenticate(username=username, password=password)
    #
    #     if user is not None:
    #         auth.login(request, user)
    #         # messages.info(request, f"You are now logged in as {username}")
    #         if user.groups.exists():
    #             return render(request, 'account.html')
    #             # return redirect('account')
    #         else:
    #             messages.info(request, 'Admin Role not assigned yet, but account is created')
    #
    #     else:
    #         messages.info(request, 'Invalid Credentials.')
    #         return redirect('/')
    #
    #
    #     # form = AuthenticationForm(request, data=request.POST)
    #     # if form.is_valid():
    #     #     username = form.cleaned_data('username')
    #     #     password = form.cleaned_data('password')
    #     #     user = authenticate(username, password)
    #     #     if user is not None:
    #     #         login(request, user)
    #     #         messages.info(request, f"You are now logged in as {username}")
    #     #         if user.groups.exists():
    #     #             return render(request, 'account.html')
    #     #         else:
    #     #             messages.info(request, 'Admin Role not assigned yet, but account is created')
    #     #
    #     #     else:
    #     #         messages.info(request, 'Invalid Credentials.')
    #     #         return redirect('/')
    #
    #     # else:
    #     #     messages.info(request, 'Invalid Credentials.')
    #     #     return redirect('/')
    # return render(request, 'home.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.groups.exists():
                    return redirect('account page')
            # globalUrls = Link.objects.filter(links__name='Global')  # returns queryset using foreign key to where group is Global
            # userGroup = user.groups.all()[0]  # object

            # if (userGroup.name != "Global"):
            #     userUrls = Link.objects.filter(links__name=userGroup.name)  # queryset
            #     links = list(chain(globalUrls, userUrls))  # concat querysets
            #     context = {'links': links, 'Role': userGroup.name}
            # else:
            #     context = {'links': globals}
            # return render(request, 'account.html', context)

            # links = Link.objects.all()
            # category = user.get_group_permissions()
            # category = Group.

            # return render(request, 'account.html', {'links': links}, {'category': category})
            # return render(request, 'account.html', {'links': links})
        else:
            messages.info(request, 'Invalid Credentials.')
            return redirect('/')

    else:
        return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')

def accountPage(request):
    user=request.user
    globalUrls = Link.objects.filter(links__name='Global')  # returns queryset using foreign key to where group is Global
    userGroup = user.groups.all()[0]  # object

    if (userGroup.name != "Global"):
        userUrls = Link.objects.filter(links__name=userGroup.name)  # queryset
        links = list(chain(globalUrls, userUrls))  # concat querysets
        context = {'links': links, 'Role': userGroup.name}
    else:
        context = {'links': globalUrls,'Role':userGroup.name}
    return render(request, 'account.html', context)
