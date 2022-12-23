from django.http import HttpResponse
from django.shortcuts import render
from .forms import Login

def index(request):
    return render(request,'home/index.html' )


def login(request):
    form = Login()
    # pegar os valores do form que são o username e password
    # buscar usuário no banco(model) com o username e checar se a senha é igual
    return render(request,'login/index.html',{"form": form} )