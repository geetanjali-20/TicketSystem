from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index', views.index, name='index'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('newuser', views.newuser, name='newuser'), 
    path("register",views.registeruser, name='register'),
    path('ticket/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id')
]
