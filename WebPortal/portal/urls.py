from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_request,name='login'),
    path('adminPage',views.adminPage,name='admin page')
]