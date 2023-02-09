from django import forms

from app_blog.models import Post


class PostForm(forms.ModelForm):
    images_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'images_field']


class UploadPostForm(forms.Form):
    file = forms.FileField(help_text='Post(s) for upload')
