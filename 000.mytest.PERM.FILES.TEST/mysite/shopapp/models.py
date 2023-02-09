from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    class Meta:
        ordering = ['-name', 'price'] # сортировка (так же влияет на связные таб.)
        # db_table = 'tech_products' # через какую табл запрашивать данные
        # verbose_name_plural = 'products' # как писать если во множественном числе

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    small_num = models.PositiveSmallIntegerField(default=0)
    reg_time = models.DateTimeField(auto_now_add=True)
    premium = models.BooleanField(default=False)

    # @property
    # def description_short(self) -> str:
    #     if len(self.description) < 48:
    #         return self.description
    #     return self.description[:48] + '...'

    def __str__(self) -> str:
        return f'Product(pk={self.pk}, name={self.name!r})'


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='order')
