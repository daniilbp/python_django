from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User, Group


class MainView(View):

    def get(self, request):
        group = Group.objects.filter(id=request.user.id).first()
        return render(request, 'main.html', {'group': str(group)})
