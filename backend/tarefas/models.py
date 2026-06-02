from django.db import models
from usuarios.models import Usuario
from professores.models import Professor


class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não urgente'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ABERTA'
    )

    prioridade = models.CharField(
        max_length=20,
        choices=PRIORIDADE_CHOICES,
        default='NAO_URGENTE'
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_entrega = models.DateField()

    usuario_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    professor_responsavel = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tarefas_criadas"
    )

    cancelada_por = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tarefas_canceladas"
    )

    data_cancelamento = models.DateTimeField(null=True, blank=True)

    def cancelar(self, professor):
        from django.utils import timezone

        self.status = 'CANCELADA'
        self.cancelada_por = professor
        self.data_cancelamento = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo