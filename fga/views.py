from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
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
    if request.method == "GET":
        return render(request, 'login/index.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha invalidos')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse('Já existe usuario com esse email.')

        user = User.objects.create_user(username=username, email = email, password=senha)
        user.save()

        return HttpResponse('Usuario cadastrado')