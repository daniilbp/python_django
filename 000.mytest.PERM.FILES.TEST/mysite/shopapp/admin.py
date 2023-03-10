from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Product, Order
from .admin_mixins import ExportAsCSVMixin


class OrderInline(admin.TabularInline):
    model = Product.order.through


@admin.action(description='Archive(premium) products')
def mark_premium(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(premium=True)

@admin.action(description='Unarchive(un-premium) products')
def mark_unpremium(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(premium=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [mark_premium, mark_unpremium, 'export_csv',]
    inlines = [OrderInline,]
    # list_display = 'pk', 'name', 'description', 'price', 'small_num'
    list_display = 'pk', 'name', 'description_short', 'price', 'small_num', 'premium'
    list_display_links = 'pk', 'name'
    ordering = '-name', 'pk'
    search_fields = 'name', 'description', 'price'
    fieldsets = [
        (None, {
            'fields': ('name', 'description'),
        }),
        ('Price options', {
            'fields': ('price', 'small_num'),
            'classes': ('collapse', 'wide'),
        }),
        ('Extra options', {
            'fields': ('premium',),
            'classes': ('collapse',),
            'description': 'asf af afkj alkfjask fjaskljd laskjd adja klj'
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'

# admin.site.register(Product, ProductAdmin)


# class ProductInline(admin.TabularInline): # v1 отобрражение
class ProductInline(admin.StackedInline): # v2 отображение
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]
    list_display = 'delivery_address', 'promocode', 'created_at', 'user_verbose'

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
