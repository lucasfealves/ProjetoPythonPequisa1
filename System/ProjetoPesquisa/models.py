from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class User(models.Model):
    nome = models.CharField(max_length=60)
    login = models.CharField(max_length=40)
    senha = models.CharField(max_length=32)
    datainc = models.DateField(default=timezone.now())
    dataalt = models.DateField(default=timezone.now())
    
    def publish(self):
        if self.pk <= 0:
            self.datainc = timezone.now()
            self.dataalt = timezone.now()
        else:
            self.dataalt = timezone.now()
        self.save()    
    
    def __str__(self):
        return self.nome
    
class Categorias(models.Model):
    nome = models.CharField(max_length=60)
    sigla = models.CharField(max_length=30)    

    def __str__(self):
        return self.nome
    
class Produtos(models.Model):
    nome = models.CharField(max_length=110)
    categoria = models.ForeignKey('Categorias')
    preco = models.FloatField()
    situacao = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome