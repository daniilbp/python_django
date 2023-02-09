from django.urls import path
from app_users.views import (
    UserLoginView,
    UserLogoutView,
    register_view,
    user_account,
    # update_profile,
    AccountUpdateView,
)
from myblog.views import MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/<int:pk>/', user_account, name='account'),
    path('account/<int:pk>/update_account/', AccountUpdateView.as_view(), name='account_update_form'),
    # path('account/<int:pk>/update_account/', update_profile, name='account_update_form'),
]