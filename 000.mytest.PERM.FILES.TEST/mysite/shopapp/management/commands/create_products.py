from shopapp.models import Product
from django.core.management.base import BaseCommand
import random
import datetime


class Command(BaseCommand):
    help = 'создает новый продукт'

    # def add_arguments(self, parser):
    #     parser.add_argument('-N', '--name', type=str, help='Название продукта')
    #     parser.add_argument('-P', '--price', type=float, help='Цена продукта')

    def handle(self, *args, **kwargs):
        self.stdout.write('Create products') # вывод инфо

        # name = kwargs['name']
        # price = kwargs['price']
        #
        # Product.objects.get_or_create(article=random.randint(1, 9999), name=name, price=price)

        #2 product, created = Product.objects.get_or_create(article=random.randint(1, 9999), name=input('Введите название продукта: '), price=float(input('Введите цену продукта: ')))
        # print(created)
        # print(product)

        #3 Skillbox exm
        products_name = ['Laptop2', 'Desktop2', 'Smartphone2']
        for product_name in products_name:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f'Created product {product.name}')

        self.stdout.write(self.style.SUCCESS('Products created')) # инфо по выполнению + стиль
