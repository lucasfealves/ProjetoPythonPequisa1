from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorias, Produtos
from .forms import CategoriaForm, ProdutosForm
#import pymsgbox
#from tkinter import messagebox
#import tkinter

# Create your views here.
def home(request):
    return render(request, 'ProjetoPesquisa/home.html', {})
def Categoria(request):
    categorias = Categorias.objects.order_by('nome')
    return render(request, 'ProjetoPesquisa/Categoria.html', {'categorias': categorias})
def Categoria_new(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('Categoria')
    else:
        form = CategoriaForm()
    return render(request, 'ProjetoPesquisa/categoria_edit.html', {'form': form})
def Categoria_edit(request, pk):
    categoria = get_object_or_404(Categorias, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('Categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'ProjetoPesquisa/categoria_edit.html', {'form': form})    
def Categoria_delete(request, pk):
    categoria = get_object_or_404(Categorias, pk=pk)
    categoria.delete()
    # response = pymsgbox.confirm(text='Deseja realmente deletar este registro', title='Alerta de Sistema', buttons=['OK', 'Cancel'])
    #response = messagebox.askyesno('Alerta de Sistema','Deseja realmente deletar este registro?')
    #sleep(1000)
    #if response:
    return redirect('Categoria')
def Produto(request):
    produtos = Produtos.objects.order_by('nome')
    return render(request, 'ProjetoPesquisa/Produto.html', {'produtos':  produtos})
def Produtos_new(request):
    if request.method == "POST":
        form = ProdutosForm(request.POST)
        if form.is_valid():
            produtos = form.save(commit=False)
            produtos.save()
            return redirect('Produtos')
    else:
        form = ProdutosForm()
    return render(request, 'ProjetoPesquisa/produto_edit.html', {'form': form})
def Produtos_edit(request, pk):
    produtos = get_object_or_404(Produtos, pk=pk)
    if request.method == "POST":
        form = ProdutosForm(request.POST, instance=produtos)
        if form.is_valid():
            produtos = form.save(commit=False)
            produtos.save()
            return redirect('Produtos')
    else:
        form = ProdutosForm(instance=produtos)
    return render(request, 'ProjetoPesquisa/produto_edit.html', {'form': form})    
def Produtos_delete(request, pk):
    produtos = get_object_or_404(Produtos, pk=pk)
    produtos.delete();
    return redirect('Produtos')
