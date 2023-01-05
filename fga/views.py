from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import Login
from .models import User


def index(request):

    return render(request,'home/index.html' )


def login(request):

    form = Login()
    #(X) pegar os valores do form que são o username e password
    #(X) buscar usuário no banco(model) com o username e checar se a senha é igual

    if request.method == "POST":
        form = Login(request.POST)
        #usuario = User(name='a', age='23', username='teste',password='senha')
        #usuario.save()
                
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            

            if User.objects.filter(username=username):

                user = User.objects.get(username=username)
                
                if user.username == username:
                    if user.password == password:
                        #return render(request,'login/test.html',)
                        pass
                else:
                    form = Login()
            else:
                form = Login()
                        
        else:
            form = Login()
    else:
        form = Login()

    return render(request,'login/index.html',{"form": form} )