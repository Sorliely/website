from django.db import models
from django.urls import reverse


class Cookie(models.Model):
    """БД истории"""
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True) #время создание записи
    time_update = models.DateTimeField(auto_now=True) #время обновления
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        """выводит название записей в бд """
        return self.title

    class Meta:
        verbose_name = 'Популярные печенья'
        verbose_name_plural = 'Популярные печенья'
        ordering = ['time_create', 'title']

class Recipe(models.Model):
    """БД рецептов"""
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)  # время создание записи
    time_update = models.DateTimeField(auto_now=True)  # время обновления
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    """Эта БД связывает все остальные"""
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})