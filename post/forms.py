#!usr/local/bin
# coding: latin-1

from django import forms
from .models import Post, Comentario


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'categoria', 'imagen', 'autor']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input'}),
            'contenido': forms.Textarea()
        }


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = '__all__'
