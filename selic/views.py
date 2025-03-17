from rest_framework import viewsets
from django.utils.timezone import now
from .models import SelicRate
from .serializers import SelicRateSerializer
from .permissions import ReadOnlyOrAuthenticated  # Importando a permissão personalizada
from django.shortcuts import render


class SelicRateViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar taxas Selic.
    Permite GET para todos, mas POST, PUT e DELETE exigem autenticação.
    """
    serializer_class = SelicRateSerializer
    permission_classes = [ReadOnlyOrAuthenticated]  # Aplicando a permissão personalizada

    def get_queryset(self):
        return SelicRate.objects.filter(data__lte=now()).order_by('-data')

# Função index para a página inicial

def index(request):
    taxas_selic = SelicRate.objects.all().order_by('-data')  # Pegando todas as taxas ordenadas
    return render(request, 'selic/index.html', {'taxas': taxas_selic})  # Passando os dados para o template