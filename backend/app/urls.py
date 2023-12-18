from django.contrib import admin
from django.urls import path,include
from .views import *
from chats.views import get_user_list

urlpatterns = [
    path('register/', register_user,name="register"),
    path('login/', login,name="login"),
    path('users/', get_user_list,name="users"),
    ]