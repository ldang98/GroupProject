from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, '\nERROR: Username already exists\n')
                # return redirect('sign_up')
            if User.objects.filter(email=email).exists():
                messages.info(request, '\nERROR: Email already taken\n')
                # return redirect('sign_up')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, '\nUser created successfully\n')

            # return redirect('sign_up')

        if password1 != password2:
            messages.info(request, '\nERROR: password not matching\n')
            # return redirect('sign_up')

        return redirect('sign_up')
        # return redirect('/')

    else:
        return render(request, 'sign_up.html')
