from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

class Course(models.Model):
    title = models.CharField(max_length=25)
    duration = models.IntegerField()
    description = models.CharField(max_length=150)
    credit_number = models.IntegerField()
    icon = models.CharField(max_length=150)