from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey welcome to the site.\nLogin or Register here.")