from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст новости')
    publisher = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    created_at = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    is_active = models.BooleanField(verbose_name='Активность', default=False)


    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        permissions = {
            ("can_verify", "Может проверить"),
        }

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Какой новости')
    name = models.CharField(default='anonim', max_length=100, verbose_name='Автор')
    comment_text = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text
