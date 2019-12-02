from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Link

from django.http import HttpResponse


# Son's Code
# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user) #have code here that decides which page to go to based on group 
#             if user.groups.filter(name='Global').exists():
#                 return render(request, 'Global.html')
#             elif user.groups.filter(name='Finance').exists():
#                 return render(request, 'account.html')
#             elif user.groups.filter(name='Sales').exists():
#                 return render(request, 'SalesTemplate.html')
#             elif user.groups.filter(name='HR').exists():
#                 return render(request, 'HRTemplate.html')
#             elif user.groups.filter(name='Engineering').exists():
#                 return render(request, 'EngineeringTemplate.html')
#             else:
#                 messages.info(request, 'Admin Role not assigned yet, but account is created')
#                 return redirect('/')
#         else:
#             messages.info(request, 'Invalid Credentials.')
#             return redirect('/')
#     else:
#         return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def login_request(request):
    if(request.method=='POST'):
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data('username')
            password=form.cleaned_data('password')
            user=authenticate(username,password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                if user.groups.exists():
                    return redirect('admin page')
                else:
                    messages.info(request, 'Admin Role not assigned yet, but account is created')
                    
            else:
               messages.info(request, 'Invalid Credentials.')
               
        else:
            messages.info(request, 'Invalid Credentials.')
    return render(request, 'home.html')
def adminPage(request):
    currentUser=request.user
    globalUrls=Link.objects.filter(links__name='Global')#returns queryset using foreign key to where group is Global
    userGroup=currentUser.groups.all()[0]#object
    
    if(userGroup.name != "Global"):
        userUrls=Link.objects.filter(links__name=userGroup.name)#queryset
        allUrls=list(chain(globalUrls,userUrls))#concat querysets
        context={'all_urls':allUrls,'Role':userGroup.name}
    else:
        context={'all_urls':globals}
    return render(request, 'testPage.html',context)
    
