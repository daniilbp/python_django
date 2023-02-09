from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from app_users.forms import AuthForm, RegisterForm, ResorePasswordForm
from app_users.models import Profile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


import datetime


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            auth_time = datetime.datetime.now()
            if 22 >= auth_time.hour >= 8:
                if user:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('Вы успешно вошли в систему')
                    else:
                        auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна!')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Запретит логина на сайте с 22:00 до 8:00')
    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из своей учетной записи')


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            discount_card = form.cleaned_data.get('discount_card')
            phone_number = form.cleaned_data.get('phone_number')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                discount_card=discount_card,
                phone_number=phone_number
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_account(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/account.html')


def restore_password(request):
    if request.method == 'POST':
        restore_password_form = ResorePasswordForm(request.POST)
        if restore_password_form.is_valid():

            new_password = User.objects.make_random_password()
            user_email = restore_password_form.cleaned_data['email']
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Восстановление пароля',
                message='Test',
                from_email='admin@company.com',
                recipient_list=[restore_password_form.cleaned_data['email']]
            )
            return HttpResponse('Письмо было успешно отправлено с новым паролем!')
    restore_password_form = ResorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'users/restore_password.html', context=context)
