from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from app_news.forms import NewsForm, Comment1Form, Comment2Form
from app_news.models import News, Comment
from app_users.models import Profile


# @permission_required('app_news.view_news')
def news_list(request):
    filter_for_list = 'created_at'
    if request.method == 'POST':
        filter_for_list = request.POST['format']
    news = News.objects.order_by(filter_for_list)
    return render(request, 'app_news/news_list.html', {'news_list': news})


@permission_required('app_news.change_news')
def news_list_moder(request):
    news = News.objects.all()
    return render(request, 'app_news/news_list_moder.html', {'news_list': news})


# class NewsDetailsView(DetailView):
#     template_name = "app_news/news_detail.html"
#     model = News
#     context_object_name = "news"


def news_details(request: HttpRequest, pk) -> HttpResponse:
    if request.method == 'POST':
        news = News.objects.get(pk=pk)
        if request.user.is_authenticated:
            form = Comment1Form(request.POST)
            if form.is_valid():
                user = request.user
                name = request.user.first_name
                news = news
                comment_text = form.cleaned_data['comment_text']
                Comment.objects.create(user=user, name=name, news=news, comment_text=comment_text)
                url = reverse('app_news:news_details', kwargs={"pk": pk})
                return redirect(url)
        else:
            form = Comment2Form(request.POST)
            if form.is_valid():
                # user,_ = User.objects.get_or_create(username="guest")
                news = news
                name = form.cleaned_data['name']
                comment_text = form.cleaned_data['comment_text']
                Comment.objects.create(name=name, news=news, comment_text=comment_text)
                url = reverse('app_news:news_details', kwargs={"pk": pk})
                return redirect(url)
    else:
        news = News.objects.get(pk=pk)
        if request.user.is_authenticated:
            form = Comment1Form()
        else:
            form = Comment2Form()
    context = {
        'form': form,
        'comments': Comment.objects.filter(news=news),
        'news': news,
    }
    return render(request, 'app_news/news_detail.html', context=context)


@login_required
@permission_required('app_news.add_news')
def create_news(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            num_news = request.user.profile.num_news + 1
            Profile.objects.filter(user=request.user).update(
                num_news=num_news
            )
            author = request.user
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publisher = form.cleaned_data['publisher']
            News.objects.create(author=author, title=title, content=content, publisher=publisher)
            # form.save()
            url = reverse('app_news:news_list')
            return redirect(url)
    else:
        form = NewsForm()
    context = {
        "form": form
    }
    return render(request, 'app_news/news_form.html', context=context)


# class NewsCreateView(PermissionRequiredMixin, CreateView):
#     permission_required = 'app_news.add_news'
#     model = News
#     fields = "title", "content", "publisher"
#     success_url = reverse_lazy("news_list")


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_news.change_news'
    model = News
    fields = "title", "content", "publisher"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("app_news:news_details", kwargs={"pk": self.object.pk},)


class NewsDetailsModerView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_news.change_news'
    model = News
    fields = "title", "content", "publisher", "is_active"
    template_name_suffix = "_detail_moder"

    def get_success_url(self):
        return reverse("app_news:news_details", kwargs={"pk": self.object.pk},)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_news.delete_news'
    model = News
    success_url = reverse_lazy("app_news:news_list")

    # def update_num_news(self, request: HttpRequest):
    #     num_news = request.user.profile.num_news - 1
    #     Profile.objects.filter(user=request.user).update(
    #         num_news=num_news
    #     )


# class EArticleView(View):
#     template_name = 'app_news/news_detail.html'
#     comment_form = CommentForm
#
#     def get(self, request, *args, **kwargs):
#         news = get_object_or_404(News, id=self.kwargs['article_id'])
#         context = {}
#         context.update(csrf(request))
#         user = auth.get_user(request)
#         # Помещаем в контекст все комментарии, которые относятся к статье
#         # попутно сортируя их по пути, ID автоинкрементируемые, поэтому
#         # проблем с иерархией комментариев не должно возникать
#         context['comments'] = news.comment_set.all().order_by('path')
#         context['next'] = news.get_absolute_url()
#         # Будем добавлять форму только в том случае, если пользователь авторизован
#         if user.is_authenticated:
#             context['form'] = self.comment_form
#
#         return render_to_response(template_name=self.template_name, context=context)
#
#
# # Декораторы по которым, только авторизованный пользователь
# # может отправить комментарий и только с помощью POST запроса
# @login_required
# @require_http_methods(["POST"])
#
# def add_comment(request, article_id):
#
#     form = CommentForm(request.POST)
#     news = get_object_or_404(News, id=article_id)
#
#     if form.is_valid():
#         comment = CommentV2()
#         comment.path = []
#         comment.article_id = news
#         comment.author_id = auth.get_user(request)
#         comment.content = form.cleaned_data['comment_area']
#         comment.save()
#
#         # Django не позволяет увидеть ID комментария по мы не сохраним его,
#         # хотя PostgreSQL имеет такие средства в своём арсенале, но пока не будем
#         # работать с сырыми SQL запросами, поэтому сформируем path после первого сохранения
#         # и пересохраним комментарий
#         try:
#             comment.path.extend(CommentV2.objects.get(id=form.cleaned_data['parent_comment']).path)
#             comment.path.append(comment.id)
#         except ObjectDoesNotExist:
#             comment.path.append(comment.id)
#
#         comment.save()
#
#     return redirect(news.get_absolute_url())
