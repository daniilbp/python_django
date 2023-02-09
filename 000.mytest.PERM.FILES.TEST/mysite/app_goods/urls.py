from django.urls import path
from app_goods.views import items_list, update_prices, ItemDetailView


urlpatterns = [
    path('items/', items_list, name='items_list'),
    path('update_prices/', update_prices, name='update_prices'),
    path('items/<int:pk>', ItemDetailView.as_view(), name='item_detail'),
]
