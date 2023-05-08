from django.contrib import admin
from .models import *

class CookieAdmin(admin.ModelAdmin):
    #содержит список полей которые мы хотим видить в админке
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    #содержит поля на которые можно нажимать для редактирования
    list_display_links = ('id', 'title')
    #содержит информация по каким полям можно осуществлять поиск
    search_fields = ('title', 'content')
    # заполняет автоматически поле slug на основе имени
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Cookie, CookieAdmin)
admin.site.register(Recipe, CookieAdmin)
admin.site.register(Category, CategoryAdmin)

