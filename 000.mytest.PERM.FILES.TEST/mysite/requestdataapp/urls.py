from django.urls import path
from .views import process_get_view, user_form, handle_file_upload

app_name = 'requestdataapp'
urlpatterns = [
    path('get/', process_get_view, name='det-view'),
    path('bio/', user_form, name='user-form'),
    path('upload/', handle_file_upload, name='upload'),
    # path('orders/', orders_list, name='orders_list'),
]
