from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)