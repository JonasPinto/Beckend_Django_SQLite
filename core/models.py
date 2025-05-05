from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preço = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    esstoque = models.IntegerField('Estoque')
    
    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.PositiveIntegerField('Telefone', max_length=11)
    
    

