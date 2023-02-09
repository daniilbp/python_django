from django.shortcuts import render
from app_goods.models import Item
from app_goods.forms import UploadPriceForm
from django.http import HttpResponse, HttpRequest
from csv import reader
from decimal import Decimal

from django.views.generic import DetailView


def items_list(request):
    items = Item.objects.all()
    return render(request, 'app_goods/items_list.html', {'items_list': items})


def update_prices(request):
    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode("utf-8").split('\n')
            update_goods = 0

            if price_str[-1] == '':
                price_str = price_str[:-1]
                csv_reader = reader(price_str, delimiter=";", quotechar='"')
            else:
                csv_reader = reader(price_str, delimiter=":", quotechar='"')

            non_update_list = [item.code for item in Item.objects.all()]

            for row in csv_reader:
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                update_goods += 1
                non_update_list.remove(row[0])

            non_update_goods = len(Item.objects.all()) - update_goods

            upload_file_form.save()
            return HttpResponse(content=(
                'Количество обновленных товаров: ', update_goods,
                ' | Количество необновленных товаров: ', non_update_goods,
                ' | Aртикулы товаров, которых не было в базе данных: ', non_update_list
            ), status=200)
    else:
        upload_file_form = UploadPriceForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'app_goods/upload_price_file.html', context=context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'app_goods/item_detail.html'
    context_object_name = 'item'
