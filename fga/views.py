from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Noticia, Equipe, Empresa




def index(request):
    noticias = Noticia.objects.all()[:4]
    return render(request,'home/index.html',{"noticias": noticias} )

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
        print(bool(user))
        if user:
            login(request, user)
            return render(request,'administracao/index.html')
        else:
            messages.success(request, "Email ou senha invalidos")
            return redirect('login')

#cadastro usuario
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html', {})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()

        if user:
            message = { 'status': -1, 'message': 'Este usuário já foi cadastrado!'}
            return render(request, 'cadastro/index.html', message)

        user = User.objects.create_user(username=username, email = email, password=senha)
        user.save()

        message = { 'status': -1, 'message': 'Usuário cadastrado!'}
        return render(request, 'cadastro/index.html', message)

#cadastrar noticias
def cad_noticia(request):
    if request.method == "GET":
        return render(request, 'cadastrar/noticias/index.html', {})
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        descricao = request.POST.get('descricao')

        noticia = Noticia.objects.filter(titulo=titulo).values() # impedir que envie duas vezes a mesma notícia.
        
        if noticia:
            message = { 'status': -1, 'message': 'A noticia já existe!'}
            return render(request, 'cadastrar/noticias/index.html', message)

        noticia = Noticia.objects.create(titulo=titulo, subtitulo=subtitulo, descricao=descricao)
        noticia.save()
        message = { 'status': 1, 'message': 'Noticia cadastrada com sucesso!'}
        return render(request, 'cadastrar/noticias/index.html', message)

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

    noticias = Noticia.objects.all()
    return render(request,'listar/noticia/index.html', { "noticias": noticias})

#cadastrar equipes
def cad_equipe(request):
    if request.method == "GET":
        return render(request, 'cadastrar/equipe/index.html', {})
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        texto = request.POST.get('texto')
        redes = request.POST.get('redes')
        link = request.POST.get('link')

        equipe = Equipe.objects.filter(titulo=titulo).values()

        print(str(equipe))

        if equipe:
            message = { 'status': -1, 'message': 'A equipe já existe!'}
            return render(request, 'cadastrar/equipe/index.html', message)

        equipe = Equipe.objects.create(titulo=titulo, subtitulo=subtitulo, texto=texto, redes=redes, link=link)
        equipe.save()
        message = { 'status': 1, 'message': 'Equipe cadastrada com sucesso!'}
        return render(request, 'cadastrar/equipe/index.html', message)

#listar equipe
def ler_equipe(request):
    equipes = Equipe.objects.all()
    return render(request,'listar/equipe/index.html', {"equipes": equipes})


#cadastrar empresas
def cad_empresa(request):
    if request.method == "GET":
        return render(request, 'cadastrar/Empresa/index.html', {})
    else:
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        texto = request.POST.get('texto')
        redes = request.POST.get('redes')
        link = request.POST.get('link')

        empresa = Empresa.objects.filter(texto=texto).first()

        if empresa:
            message = { 'status': -1, 'message': 'A empresa já existe!'}
            return render(request, 'cadastrar/empresa/index.html', message)

        empresa = Empresa.objects.create(titulo=titulo, subtitulo=subtitulo, texto=texto, redes=redes, link=link)
        empresa.save()
        message = { 'status': 1, 'message': 'Empresa cadastrada com sucesso!' }
        return render(request, 'cadastrar/empresa/index.html', message)

#listar empresa
def ler_empresa(request):
    empresas = Empresa.objects.all()
    return render(request,'listar/empresa/index.html', {"empresas": empresas})

def administracao(request):
    return render(request, 'administracao/index.html')

def pagina_nao_encontrada(request, exception):
    return render(request, 'errors/page_not_found.html')