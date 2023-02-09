from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import UpdateView

from app_users.forms import RegisterForm, UploadAvatarForm #, UpdateProfileForm
from app_users.models import Profile


class UserLoginView(LoginView):
    template_name = 'main_login.html'


class UserLogoutView(LogoutView):
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        form_for_avatar = UploadAvatarForm(request.POST, request.FILES)
        if form.is_valid() and form_for_avatar.is_valid():
            avatar = form_for_avatar.cleaned_data.get('avatar')
            user = form.save()
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            Profile.objects.create(
                user=user,
                name=name,
                surname=surname,
                avatar=avatar
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            url = reverse('account', kwargs={"pk": user.id})
            return redirect(url)
    else:
        form_for_avatar = UploadAvatarForm()
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form, 'form_for_avatar': form_for_avatar})


def user_account(request: HttpRequest, pk) -> HttpResponse:
    group = Group.objects.filter(id=request.user.id).first()
    return render(request, 'app_users/account.html', {'group': group})


class AccountUpdateView(UpdateView):
# class AccountUpdateView(PermissionRequiredMixin, UpdateView):
#     permission_required = 'app_users.change_profile'
    model = Profile
    fields = "name", "surname", "avatar"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("account", kwargs={"pk": self.object.pk},)


# @login_required
# def update_profile(request, pk):
#     if request.method == 'POST':
#         form = UpdateProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             avatar = form.cleaned_data.get('avatar')
#             name = form.cleaned_data.get('name')
#             surname = form.cleaned_data.get('surname')
#             Profile.objects.filter(user=request.user).update(
#                 name=name,
#                 surname=surname,
#                 avatar=avatar
#             )
#             form.save()
#             url = reverse('account', kwargs={"pk": request.user.id})
#             return redirect(url)
#     else:
#         form = UpdateProfileForm()
#     return render(request, 'app_users/profile_update_form.html', {'form': form})

