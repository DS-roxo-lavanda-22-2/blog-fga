from django.contrib import admin
from .models import Noticia
from .models import Login, Equipe

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Login)
admin.site.register(Equipe)