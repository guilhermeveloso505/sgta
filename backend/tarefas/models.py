from django.db import models
from usuarios.models import Usuario

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
        ('URGENTE', 'NAO_URGENTE')
    ]
    
    titulo = models.CharField(max_length=255,)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    usuario_responsavel = models.ForeignKey(to=Usuario, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.titulo

# Create your models here.
