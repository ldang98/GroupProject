from django.urls import path

from . import views

urlpatterns=[
    # path('', views.account, name='users'),
    path('', views.logout, name='users'),
]