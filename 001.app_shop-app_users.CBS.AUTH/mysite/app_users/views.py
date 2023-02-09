from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from app_users.forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView

import datetime


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'
