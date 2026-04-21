from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuario = Usuario.objects.all().values()
    return JsonResponse(list[any](usuario), safe=False)
 
# Create your views here.
