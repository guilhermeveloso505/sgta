from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=str)
    ativo = models.BooleanField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

# Create your models here.
