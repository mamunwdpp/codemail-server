from django.contrib import admin
from django.urls import path, include
from.views import checkUser
urlpatterns = [
    path('code/mail/', checkUser, name="checkUser"),
]