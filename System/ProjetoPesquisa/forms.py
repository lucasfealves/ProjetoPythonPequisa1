'''
Created on 24 de jan de 2017

@author: Lucas Felipe Alves
'''
from django import forms
from .models import Categorias, Produtos

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = ('nome', 'sigla',)
        
class ProdutosForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ('nome', 'categoria', 'preco', 'situacao')        