from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=500, null=True)
    descricao = models.TextField(null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.TextField(max_length=20000, null=True)

class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Equipe(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length= 500)
    texto= models.TextField()
    redes = models.CharField(max_length= 20)
    link = models.CharField(max_length=200)

class Empresa(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length= 500)
    texto= models.TextField()
    redes = models.CharField(max_length= 20)
    link = models.CharField(max_length=200)
