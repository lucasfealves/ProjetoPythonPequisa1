'''
Created on 24 de jan de 2017

@author: Lucas Felipe Alves
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^Systema/AskMessage/(?P<message>[^/]+)/(?P<prev_link>[^/]+)/(?P<action_link>[^/]+)/(?P<pk>[0-9]+)/$', views.AskMessageLocal, name='AskMessage'),
    url(r'^Systema/AskMessage/$', views.AskMessage),
    url(r'^Categoria/$', views.Categoria, name='Categoria'),
    url(r'^Categoria/new/$', views.Categoria_new, name='CategoriaNew'),
    url(r'^Categoria/(?P<pk>[0-9]+)/edit/$', views.Categoria_edit, name='CategoriaEdit'),
    url(r'^Categoria/(?P<pk>[0-9]+)/delete/$', views.Categoria_delete, name='CategoriaDelete'),
    url(r'^Produtos/$', views.Produto, name='Produtos'),
    url(r'^Produtos/new/$', views.Produtos_new, name='ProdutosNew'),
    url(r'^Produtos/(?P<pk>[0-9]+)/edit/$', views.Produtos_edit, name='ProdutosEdit'),
    url(r'^Produtos/(?P<pk>[0-9]+)/delete/$', views.Produtos_delete, name='ProdutosDelete'),
    
]