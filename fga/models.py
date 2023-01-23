from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length= 500)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email