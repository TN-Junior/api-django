from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.utils.timezone import now
from .models import SelicRate
from .serializers import SelicRateSerializer

# Definição da ViewSet corretamente sem imports circulares
class SelicRateViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar taxas Selic.
    Apenas usuários autenticados podem modificar os dados.
    """
    serializer_class = SelicRateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Retorna apenas taxas Selic com datas válidas, ordenadas por data decrescente.
        """
        return SelicRate.objects.filter(data__lte=now()).order_by('-data')

# Função index para a página inicial

def index(request):
    taxas_selic = SelicRate.objects.all().order_by('-data')  # Pegando todas as taxas ordenadas
    return render(request, 'selic/index.html', {'taxas': taxas_selic})  # Passando os dados para o template