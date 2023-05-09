from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


def index(request):
    """главная страница"""
    posts = Cookie.objects.all()
    context = {'posts': posts,
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
    """функция авторизации
    выполняет фунуцию приема данных и если данные ошибочные возвращает
    их пользователю"""
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            #добавление новой записи в бд
            try:
                Cookie.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm
    return render(request, 'cookie/addpage.html', {'form': form, 'title': 'Добавление статьи'})

def login(request):
    return HttpResponseNotFound("Автаризация")

# def show_post(request, post_id):
#     return HttpResponseNotFound(f'Отображает статьи с id = {post_id}')

def pageNotFound(request, exception):
    """отоброжение ошибки 404"""
    return HttpResponseNotFound("<h1>Страница не существует</h1>")

def show_post(request, post_slug):
    post = get_object_or_404(Cookie, slug=post_slug)
    context = {
        'posts': post,
        'title': 'Cookie',
        'cat_selected': post.cat_id,
    }

    return render(request, 'cookie/post.html', context=context)

def show_category(request, cat_id):
    """категориии хз зачем"""
    posts = Cookie.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'title': 'Cookie',
        'cat_selected': cat_id,
    }
    if len(posts) == 0:
        raise Http404()
    return render(request, 'cookie/index.html', context=context)