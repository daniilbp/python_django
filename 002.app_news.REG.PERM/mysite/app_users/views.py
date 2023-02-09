from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from app_users.forms import AuthForm, RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from app_users.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

import datetime


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                phone_number=phone_number
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})


def user_account(request: HttpRequest) -> HttpResponse:
    group = Group.objects.filter(id=request.user.id).first()
    return render(request, 'app_users/account.html', {'group': group})
