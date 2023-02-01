from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Noticia, Equipe




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
            return render(request,'home/index.html' )
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

def cad_noticia(request):
    if request.method == "GET":
        return render(request, 'cadastrar/noticias/index.html')
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        descricao = request.POST.get('descricao')

        noticia = Noticia.objects.filter(titulo=titulo).first() # impedir que envie duas vezes a mesma notícia.
        
        if noticia:
            return HttpResponse('Notícia já existente.')

        noticia = Noticia.objects.create(titulo=titulo, subtitulo=subtitulo, descricao=descricao)
        noticia.save()
        return HttpResponse('Notícia cadastrada')

def del_noticia(request):
    if request.method == "GET":
        return render(request, 'deletar/noticias/index.html')
    else:
        titulo = request.POST.get('titulo')

        noticia = Noticia.objects.filter(titulo=titulo).first() # pega a notícia
        
        if noticia: # checa se a notícia existe para deletar
            noticia.delete()

            return HttpResponse('Notícia já excluída.')
            
        return HttpResponse('Notícia inexistente.')


def cad_equipe(request):
    if request.method == "GET":
        return render(request, 'cadastrar/equipe/index.html')
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        texto = request.POST.get('texto')
        redes = request.POST.get('redes')
        link = request.POST.get('link')

        equipe = Equipe.objects.filter(texto=texto).first()  # impedir que envie duas vezes a mesma notícia.

        if equipe:
            return HttpResponse('Equipe já existente.')

        equipe = Equipe.objects.create(titulo=titulo, subtitulo=subtitulo, texto=texto, redes=redes,link=link)
        equipe.save()
        return HttpResponse('Equipe cadastrada')