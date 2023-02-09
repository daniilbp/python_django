from timeit import default_timer

from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import GroupForm, Comment1Form, Comment2Form
from .models import Product, Order, Comment


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2999),
            ('Smartphone', 999),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,
        }
        return render(request, 'shopapp/shop-index.html', context=context)


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm(),
            "groups": Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


# class ProductDetailsView(View):
#     def get(self, request: HttpRequest, pk: int) -> HttpResponse:
#         product = get_object_or_404(Product, pk=pk)
#         context = {
#             "product": product,
#         }
#         return render(request, "shopapp/product-details.html", context=context)


class ProductDetailsView(DetailView):
    template_name = "shopapp/product-details.html"
    model = Product
    context_object_name = "product"


# class ProductsListView(TemplateView):
#     template_name = "shopapp/products-list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = Product.objects.all()
#         return context


class ProductsListView(ListView):
    template_name = "shopapp/products-list.html"
    # model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "price", "description", "discount"
    # form_class = ProductForm # через Форму или ч/з поля
    success_url = reverse_lazy("shopapp:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = "name", "price", "description", "discount"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("shopapp:product_details", kwargs={"pk": self.object.pk},)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


# def orders_list(request: HttpRequest):
#     context = {
#         "orders": Order.objects.select_related("user").prefetch_related("products").all(),
#     }
#     return render(request, 'shopapp/order_list.html', context=context)


class OrdersListView(ListView):
    queryset = (
        Order.objects.select_related("user").prefetch_related("products")
    )


class OrdersDetailView(DetailView):
    queryset = (
        Order.objects.select_related("user").prefetch_related("products")
    )


class OrderCreateView(CreateView):
    model = Order
    fields = "delivery_address", "promocode", "user", "products"
    # form_class = OrderForm # через Форму или ч/з поля
    success_url = reverse_lazy("shopapp:orders_list")


class OrderUpdateView(UpdateView):
    model = Order
    fields = "delivery_address", "promocode", "user", "products"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("shopapp:order_details", kwargs={"pk": self.object.pk},)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("shopapp:orders_list")


class CommentsListView(ListView):
    template_name = "shopapp/comment_list.html"
    model = Comment
    context_object_name = "comments"


class CommentDetailView(DetailView):
    template_name = "shopapp/comment_detail.html"
    model = Comment
    context_object_name = "comment"


# class CommentCreateView(CreateView):
#     model = Comment
#     fields = "user", "comment_text"
#     success_url = reverse_lazy("shopapp:comments_list")


def create_comment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = Comment1Form(request.POST)
            if form.is_valid():
                comment_text = form.cleaned_data['comment_text']
                user = request.user
                name = request.user.first_name
                Comment.objects.create(user=user, name=name, comment_text=comment_text)
                url = reverse('shopapp:comments_list')
                return redirect(url)
        else:
            form = Comment2Form(request.POST)
            if form.is_valid():
                comment_text = form.cleaned_data['comment_text']
                user = User.objects.get(username="guest")
                name = form.cleaned_data['name']
                Comment.objects.create(user=user, name=name, comment_text=comment_text)
                url = reverse('shopapp:comments_list')
                return redirect(url)
    else:
        if request.user.is_authenticated:
            form = Comment1Form()
        else:
            form = Comment2Form()
    context = {
        "form": form
    }
    return render(request, 'shopapp/comment_form.html', context=context)


class CommentUpdateView(UpdateView):
    model = Comment
    fields = "name", "comment_text"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("shopapp:comment_details", kwargs={"pk": self.object.pk},)


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("shopapp:comments_list")
