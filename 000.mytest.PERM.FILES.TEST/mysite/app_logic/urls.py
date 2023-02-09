from django.urls import path
from app_logic.views import welcome


urlpatterns = [
    path('welcome/', welcome, name='welcome')
]