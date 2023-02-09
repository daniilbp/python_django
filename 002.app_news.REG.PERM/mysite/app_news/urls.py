from django.urls import path
from mysite.views import MainView
from .views import (
    news_list,
    news_list_moder,
    # NewsDetailsView,
    news_details,
    NewsDetailsModerView,
    # moder_news,
    # NewsCreateView,
    create_news,
    NewsUpdateView,
    NewsDeleteView,
    # EArticleView,
    # add_comment,
)

app_name = "app_news"

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('news_list/', news_list, name='news_list'),
    path('news_list_moder/', news_list_moder, name='news_list_moder'),
    # path("news_list/<int:pk>", NewsDetailsView.as_view(), name="news_details"),
    path("news_list/<int:pk>", news_details, name="news_details"),
    path("news_list_moder/<int:pk>", NewsDetailsModerView.as_view(), name="news_details_moder"),
    # path("news_list_moder/<int:pk>", moder_news, name="news_details_moder"),
    # path("news_list/create/", NewsCreateView.as_view(), name="news_create"),
    path("news_list/create/", create_news, name="news_create"),
    path("news_list/<int:pk>/update", NewsUpdateView.as_view(), name="news_update"),
    path("news_list/<int:pk>/confirm-delete", NewsDeleteView.as_view(), name="news_delete"),
]
