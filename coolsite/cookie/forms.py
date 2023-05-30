from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Cookie
        # можно прописывать отдельные стили для каждого метода
        # widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
