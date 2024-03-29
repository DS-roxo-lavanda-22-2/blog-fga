from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('login/', views.novo_login, name='login'),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('cadastrar/noticias/', views.cad_noticia, name = 'cad_noticia'),
    path('deletar/noticias/', views.del_noticia, name = 'del_noticia'),
    path('cadastrar/equipe/', views.cad_equipe, name = 'cad_equipe'),
    path('cadastrar/empresa/', views.cad_empresa, name = 'cad_empresa'),
    path('listar/noticias/' ,views.ler_noticia, name='ler_noticia'),
    path('listar/equipes/' ,views.ler_equipe, name='ler_equipe'),
    path('listar/empresas/' ,views.ler_empresa, name='ler_empresa'),
    path('cursos/', views.ler_cursos, name = 'ler_cursos'),
    # mostrar os cursos
    path('cursos/aeroespacial', views.show_aero, name = 'show_aero'),
    path('cursos/automotiva', views.show_auto, name = 'show_auto'),
    path('cursos/energia', views.show_ener, name = 'show_ener'),
    path('cursos/eletronica', views.show_eletro, name = 'show_eletro'),
    path('cursos/software', views.show_soft, name = 'show_soft'),

    path('gestao/', views.administracao, name='gestao')


]