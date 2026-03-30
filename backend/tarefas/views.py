from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list[any](tarefas), safe=False)
# Create your views here.
