from django.urls import path
from app_users.views import AnotherLoginView, AnotherLogoutView, register_view, user_account
from mysite.views import MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', user_account, name='account'),
]
