from django.db import models
# import os
# from django.contrib.auth import get_user_model
# from django.conf import settings
# from django.contrib.auth.models import User
from .consts import MAX_RATE
# def directory_path(instance,filename):

#     return '{0}/{1}'.format(instance.user,filename)

RATE_CHOICES=[(x,str(x)) for x in range(0,MAX_RATE+1)]

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
