from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


def user_directory_path(instance, filename):
    return 'avatars/{0}'.format(filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    num_posts = models.IntegerField(default=0)
    avatar = models.ImageField(
        upload_to=user_directory_path,
        default='/avatars/contacts-location.svg',
        verbose_name='Avatar', null=True, blank=True)

    def get_avatar(self):
        if not self.avatar:
            return '/upload/avatars/contacts-location.svg'
        return self.avatar.url

    def avatar_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_avatar())

    avatar_tag.short_description = 'Avatar pict'
