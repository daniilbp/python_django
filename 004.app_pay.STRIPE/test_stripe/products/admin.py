from django.contrib import admin

from products.models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description", "price"


admin.site.register(Item, ItemAdmin)
