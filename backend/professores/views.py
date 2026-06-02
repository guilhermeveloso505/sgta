from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Professor
from tarefas.models import Tarefa

@require_http_methods(["GET"])
def tarefas_do_professor(request, professor_id):
    tarefas = Tarefa.objects.filter(professor_responsavel_id=professor_id)

    data = list(tarefas.values(
        "id",
        "titulo",
        "status",
        "prioridade",
        "data_entrega",
        "usuario_responsavel__nome"
    ))

    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def cancelar_tarefa(request, tarefa_id):
    body = json.loads(request.body)
    professor_id = body.get("professor_id")

    professor = Professor.objects.get(id=professor_id)
    tarefa = Tarefa.objects.get(id=tarefa_id)

    tarefa.cancelar(professor)

    return JsonResponse({
        "message": "Tarefa cancelada com sucesso",
        "tarefa_id": tarefa.id
    })
    
@require_http_methods(["GET"])
def listar_professores(request):
    professores = Professor.objects.all()

    data = list(professores.values(
        "id",
        "nome",
        "email",
        "ativo"
    ))

    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def criar_professor(request):
    body = json.loads(request.body)

    professor = Professor.objects.create(
        nome=body["nome"],
        email=body["email"],
        ativo=True
    )

    return JsonResponse({
        "id": professor.id,
        "nome": professor.nome,
        "email": professor.email
    })