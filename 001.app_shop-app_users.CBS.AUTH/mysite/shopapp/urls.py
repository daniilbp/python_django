from django.urls import path
from mysite.views import MainView
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductDetailsView,
    ProductsListView,
    OrdersListView,
    OrdersDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    CommentsListView,
    CommentDetailView,
    # CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    create_comment,
)

app_name = "shopapp"

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path("index/", ShopIndexView.as_view(), name="index"),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/confirm-delete", ProductDeleteView.as_view(), name="product_delete"),
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/<int:pk>", OrdersDetailView.as_view(), name="order_details"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/update", OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/confirm-delete", OrderDeleteView.as_view(), name="order_delete"),
    path("comments/", CommentsListView.as_view(), name="comments_list"),
    path("comments/<int:pk>", CommentDetailView.as_view(), name="comment_details"),
    # path("comments/create/", CommentCreateView.as_view(), name="comment_create"),
    path("comments/create/", create_comment, name="comment_create"),
    path("comments/<int:pk>/update", CommentUpdateView.as_view(), name="comment_update"),
    path("comments/<int:pk>/confirm-delete", CommentDeleteView.as_view(), name="comment_delete"),
]
