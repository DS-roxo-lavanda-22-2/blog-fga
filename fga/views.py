from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Noticia, Equipe, Empresa




def index(request):
    return render(request,'home/index.html' )

#def index(request):
#    data = {}
#    data['logon'] = Login.objects.all()
#    form = login()
#   return render(request,'login/index.html', data)

#login usuario
def novo_login(request):
    if request.method == "GET":
        return render(request, 'login/index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse('Login realizado')
        else:
            return HttpResponse('Email ou senha invalidos')

#cadastro usuario
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

#cadastrar noticias
def cad_noticia(request):
    if request.method == "GET":
        return render(request, 'cadastrar/noticias/index.html')
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        descricao = request.POST.get('descricao')

        noticia = Noticia.objects.filter(titulo=titulo).values() # impedir que envie duas vezes a mesma notícia.
        
        if noticia:
            return HttpResponse('Notícia já existente.')

        noticia = Noticia.objects.create(titulo=titulo, subtitulo=subtitulo, descricao=descricao)
        noticia.save()
        return HttpResponse('Notícia cadastrada')

#deletar noticias
def del_noticia(request):
    if request.method == "GET":
        return render(request, 'deletar/noticias/index.html')
    else:
        titulo = request.POST.get('titulo')

        noticia = Noticia.objects.filter(titulo=titulo).first() # pega a notícia
        
        if noticia: # checa se a notícia existe para deletar
            noticia.delete()

            return HttpResponse('Notícia foi excluída.')
            
        return HttpResponse('Notícia inexistente.')

#listar noticias
def ler_noticia(request):
    data = {}

    data["dataset"] = Noticia.objects.all()

    return render(request,'listar/noticia/index.html', data)

#cadastrar equipes
def cad_equipe(request):
    if request.method == "GET":
        return render(request, 'cadastrar/equipe/index.html')
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        texto = request.POST.get('texto')
        redes = request.POST.get('redes')
        link = request.POST.get('link')

        equipe = Equipe.objects.filter(titulo=titulo).values()

        print(str(equipe))

        if equipe:
            return HttpResponse('Equipe cadastrada')

        equipe = Equipe.objects.create(titulo=titulo, subtitulo=subtitulo, texto=texto, redes=redes, link=link)
        equipe.save()
        return HttpResponse('Equipe cadastrada')

#listar equipe
def ler_equipe(request):
    data = {}

    data["dataset"] = Equipe.objects.all()

    return render(request,'listar/equipe/index.html', data)


#cadastrar empresas
def cad_empresa(request):
    if request.method == "GET":
        return render(request, 'cadastrar/empresa/index.html')
    else:
        titulo = request.POST.get('titulo')

        subtitulo = request.POST.get('subtitulo')
        texto = request.POST.get('texto')
        redes = request.POST.get('redes')
        link = request.POST.get('link')

        empresa = Empresa.objects.filter(texto=texto).first()

        if empresa:
            return HttpResponse('Empresa já existente.')

        empresa = Empresa.objects.create(titulo=titulo, subtitulo=subtitulo, texto=texto, redes=redes, link=link)
        empresa.save()
        return HttpResponse('Empresa cadastrada')

#listar empresa
def ler_empresa(request):
    data = {}

    data["dataset"] = Empresa.objects.all()

    return render(request,'listar/empresa/index.html', data)
