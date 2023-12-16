from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/', register_user,name="register"),
    path('login/', login,name="login"),
    ]