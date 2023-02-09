from csv import reader

from app_blog.models import Post, File
from app_blog.forms import PostForm, UploadPostForm

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.files.base import ContentFile
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView


def posts_list(request):
    posts_list = Post.objects.order_by('-created_at')
    return render(request, 'app_blog/posts_list.html', {'posts_list': posts_list})


@login_required
@permission_required('app_blog.add_post')
def create_post(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            images = request.FILES.getlist('images_field')
            post = Post.objects.create(user=user, title=title, content=content)
            for img in images:
                data = img.read()
                post.images.save(img.name, ContentFile(data))
                post.save()
            url = reverse('app_blog:posts_list')
            return redirect(url)
    else:
        form = PostForm()
    context = {
        "form": form
    }
    return render(request, 'app_blog/post_form.html', context=context)


@login_required
@permission_required('app_blog.add_post')
def upload_post(request):
    if request.method == 'POST':
        form = UploadPostForm(request.POST, request.FILES)
        if form.is_valid():
            post_file = form.cleaned_data['file'].read()
            post_str = post_file.decode("utf-8").split('\n')
            if post_str[-1] == '':
                post_str = post_str[:-1]
                csv_reader = reader(post_str, delimiter=";", quotechar='"')
            else:
                csv_reader = reader(post_str, delimiter=":", quotechar='"')
            for row in csv_reader:
                Post.objects.create(
                    user=request.user,
                    title=row[0],
                    content=row[1]
                )
            url = reverse('app_blog:posts_list')
            return redirect(url)
    else:
        form = UploadPostForm()
    context = {"form": form}
    return render(request, 'app_blog/upload_post.html', context=context)


class PostDetailsView(DetailView):
    template_name = 'app_blog/post_detail.html'
    model = Post
    context_object_name = "post"


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_blog.delete_post'
    model = Post
    success_url = reverse_lazy("app_blog:posts_list")


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_blog.change_post'
    model = Post
    fields = "title", "content", "images"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("app_blog:post_detail", kwargs={"pk": self.object.pk},)
