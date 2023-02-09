from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Comment


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


class Comment1Form(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]


class Comment2Form(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment_text"]
