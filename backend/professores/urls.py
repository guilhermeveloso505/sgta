from django.urls import path
from . import views

urlpatterns = [
    path("professores/", views.listar_professores),
    path("professores/criar/", views.criar_professor),
    path("professores/<int:professor_id>/tarefas/", views.tarefas_do_professor),
    path("tarefas/<int:tarefa_id>/cancelar/", views.cancelar_tarefa),
]