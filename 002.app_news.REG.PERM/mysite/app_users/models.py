from django.contrib.auth.models import User, Group
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=36, blank=True)
    city = models.CharField(max_length=36, blank=True)
    num_news = models.IntegerField(default=0)
