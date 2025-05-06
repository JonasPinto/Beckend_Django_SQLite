from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('Estoque')
    cor = models.CharField('Cor', max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f'{self.nome}'
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.PositiveIntegerField('Telefone')
    
    def __str__(self):
        return f'{self.nome}'    
    

