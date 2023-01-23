from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Login
from .forms import form_login



def index(request):
    return render(request,'home/index.html' )

#def index(request):
#    data = {}
#    data['logon'] = Login.objects.all()
#    form = login()
#   return render(request,'login/index.html', data)


def novo_login(request):
    form = form_login()
    # (X) pegar os valores do form que são o username e password
    # (X) buscar usuário no banco(model) com o username e checar se a senha é igual

    if request.method == "POST":
        form = Login(request.POST or None)

    return render(request, 'login/index.html', {"form": form})

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        return HttpResponse(username)