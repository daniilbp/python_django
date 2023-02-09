import os

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    return 'images/post_{0}/{1}'.format(instance.pk, filename)


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=30, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created date')
    images = models.ImageField(upload_to=user_directory_path, verbose_name='Images (model)', null=True, blank=True)

    def images_path(self):
        img_path = []
        if os.path.exists(os.path.abspath(f'upload/images/post_{self.pk}')):
            for image in os.listdir(os.path.abspath(f'upload/images/post_{self.pk}')):
                img_path.append(os.path.join(f'/upload/images/post_{self.pk}/{image}'))
        return img_path


class File(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Post(s) for upload')
