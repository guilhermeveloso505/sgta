from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list[any](tarefas), safe=False)
# Create your views here.

def listar_tarefas_por_status(request, status):
    status_validos = [choice[0] for choice in Tarefa.STATUS_CHOICES]
    
    if status not in status_validos:
        return JsonResponse({'erro': 'status inválido.'}, status=400)
    
    tarefas = Tarefa.objects.filter(status=status).values() # ---> filter = Realiza o filtro para a consulta, no caso anterior status = status.
    return JsonResponse(list[any](tarefas), safe=False)
