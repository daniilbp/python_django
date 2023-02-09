from django.db import models
import datetime

def user_directory_path(instance, filename):
    date_obj = datetime.datetime.now()
    date_obj_str = date_obj.strftime('%d%m%y-%H-%M-%S')
    return 'files/{0}_{1}'.format(date_obj_str, filename)

class File(models.Model):
    file = models.FileField(upload_to=user_directory_path)

class Item(models.Model):
    name = models.CharField(max_length=20, verbose_name='название', null=True)
    code = models.CharField(max_length=100, verbose_name='артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
