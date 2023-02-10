from django.contrib import admin
from .models import Login, Equipe, Empresa, Curso, Noticia

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Login)
admin.site.register(Equipe)
admin.site.register(Empresa)
admin.site.register(Curso)