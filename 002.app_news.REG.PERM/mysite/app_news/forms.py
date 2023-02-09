from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import News, Comment
from django import forms


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "publisher"]
        exclude = ["author", "created_at", "is_active"]


class Comment1Form(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]


class Comment2Form(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment_text"]
