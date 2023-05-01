from django.contrib import admin
from .models import *

class CookieAdmin(admin.ModelAdmin):
    #содержит список полей которые мы хотим видить в админке
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    #содержит поля на которые можно нажимать для редактирования
    list_display_links = ('id', 'title')
    #содержит информация по каким полям можно осуществлять поиск
    search_fields = ('title', 'content')



admin.site.register(Cookie, CookieAdmin)
admin.site.register(Recipe, CookieAdmin)
