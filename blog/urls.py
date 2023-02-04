"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from fga.views import novo_login,cadastro, cad_equipe,cad_noticia, cad_empresa, ler_noticia, ler_empresa, ler_equipe, administracao


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fga.urls')),
    path('login/', novo_login),
    path('cadastro/', cadastro),
    path('cadastrar/equipe/', cad_equipe),
    path('cadastrar/noticias/', cad_noticia),
    path('cadastrar/empresa/', cad_empresa),
    path('listar/noticias/', ler_noticia),
    path('listar/equipe/', ler_equipe),
    path('listar/empresa/', ler_empresa),
    path('gestao/', administracao),

]
