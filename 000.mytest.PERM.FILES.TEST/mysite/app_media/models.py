from django.db import models
import datetime

def user_directory_path(instance, filename):
    date_obj = datetime.datetime.now()
    date_obj_str = date_obj.strftime('%d%m%y-%H-%M-%S')
    return 'files/{0}_{1}'.format(date_obj_str, filename)

class File(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
