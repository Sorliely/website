from django.urls import path, re_path
from .views import *

"""Здесь прописываем все маршруты текущего приложения"""

urlpatterns = [
    path('', index, name='home'),
    path('history/', history, name='history'),
    path('about/', about, name='about'),
    path('login/',login, name='login'),
    path('addpage/',addpage, name='addpage'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]