from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

# Пороль от супер узера g9XSHvdtUY{2

def index(request):
    cats = Category.objects.all()
    posts = Cookie.objects.all()
    context = {'posts': posts,
               'cats': cats,
               'title': 'Cookie',
               'cat_selected': 0,
               }
    return render(request, 'cookie/index.html', context=context)

def history(request,):
    recipe = Recipe.objects.all()
    return render(request, 'cookie/history.html', {'recipe': recipe})

def about(request):
    return render(request, "cookie/about.html")

def addpage(request):
    return HttpResponseNotFound("")

def login(request):
    return HttpResponseNotFound("Автаризация")

# def show_post(request, post_id):
#     return HttpResponseNotFound(f'Отображает статьи с id = {post_id}')

def pageNotFound(request, exception):
    """отоброжение ошибки 404"""
    return HttpResponseNotFound("<h1>Страница не существует</h1>")

def show_category(request, cat_id):
    cats = Category.objects.all()
    posts = Cookie.objects.filter(cat_id=cat_id)
    context = {'posts': posts,
               'cats': cats,
               'title': 'Cookie',
               'cat_selected': cat_id,
               }
    if len(posts) == 0:
        raise Http404()
    return render(request, 'cookie/index.html', context=context)