from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length= 500)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)