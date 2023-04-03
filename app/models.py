from django.db import models

class Produtos(models.Model):
    produto = models.CharField(max_length=50)
    quantidade = models.CharField(max_length=50)
    preco = models.CharField(max_length=50)

