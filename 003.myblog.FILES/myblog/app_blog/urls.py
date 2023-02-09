from django.urls import path
from myblog.views import MainView
from app_blog.views import (
    posts_list,
    create_post,
    PostDetailsView,
    upload_post,
    PostDeleteView,
    PostUpdateView,
)


app_name = "app_blog"

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('posts_list/', posts_list, name='posts_list'),
    path('create_post/', create_post, name='create_post'),
    path('upload_post/', upload_post, name='upload_post'),
    path('posts_list/post_<int:pk>', PostDetailsView.as_view(), name='post_detail'),
    path('posts_list/post_<int:pk>/post_update', PostUpdateView.as_view(), name='post_update'),
    path('posts_list/post_<int:pk>/confirm-delete', PostDeleteView.as_view(), name='post_delete'),
]
