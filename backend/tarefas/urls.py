from django.urls import path
from .views import listar_tarefas
from .views import listar_tarefas_por_status

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/status/<str:status>', listar_tarefas_por_status)
]