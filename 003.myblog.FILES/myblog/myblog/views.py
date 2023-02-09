from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, 'main.html')


class UserLoginView(LoginView):
    template_name = 'main.html'
