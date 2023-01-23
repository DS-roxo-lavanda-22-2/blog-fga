from django.urls import path, include
# from django.contrib import admin
from . import views

urlpatterns = [
    path('login/', views.novo_login, name='login'),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name = 'cadastro')
]