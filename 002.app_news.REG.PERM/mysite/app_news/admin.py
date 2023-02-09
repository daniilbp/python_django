from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from app_news.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ['id', 'title', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def user_verbose(self, obj: News) -> str:
        return obj.user.first_name or obj.user.username


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = "user", "comment_text", "created_at"

    def user_verbose(self, obj: Comment) -> str:
        return obj.user.first_name or obj.user.username


# @admin.register(CommentV2)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = "article_id", "author_id", "content", "pub_date"
#
#     def user_verbose(self, obj: Comment) -> str:
#         return obj.user.first_name or obj.user.username
