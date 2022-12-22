from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

def index(request):
    return render(request,'home/index.html' )

def courses(request, id):
    curso = Course.objects.get(id=id)
    print(str(curso))
    return render(request, 'courses/index.html', {"course": curso })