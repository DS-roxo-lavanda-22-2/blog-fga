from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

def index(request):
    return render(request,'home/index.html' )

def courses(request):
    # curso = Course.objects.get(id=id)
    curso = {
        'title' : "Engenharia de Software",
        'duration': 16,
        'description': "A Engenharia de Software é a integração dos princípios da Matemática e Ciência da Computação com as práticas da Engenharia, com objetivo de desenvolver modelos sistemáticos e técnicas confiáveis para a produção de software de alta qualidade.",
        'credit_number': 234,
        'icon': "https://cdn-icons-png.flaticon.com/512/4882/4882524.png"
    }
    print(str(curso))

    return render(request, 'courses/index.html', {"course": curso })
