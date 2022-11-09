from django.shortcuts import render
from .models import Task


def index(request):
    articles = Task.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {'title': "Образовательная платфома", "articles": articles})


def about(request):
    return render(request, 'main/about.html')

def lib(request):
    return render(request, 'main/lib.html')

def blog(request):
    return render(request, 'main/blog.html')

def help(request):
    return render(request, 'main/help.html')

def training(request):
    return render(request, 'main/training.html')

def create(request):
    return render(request, 'main/create.html')