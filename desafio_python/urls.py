from django.urls import path, include
from rest_framework.routers import DefaultRouter
from selic.views import SelicRateViewSet, index  # Importando a função index corretamente

router = DefaultRouter()
router.register(r'selic', SelicRateViewSet, basename='selic')  # Definindo o basename corretamente

urlpatterns = [
    path('', index, name='index'),  # Certificando-se de que 'index' existe no views.py
    path('api/', include(router.urls)),  # Mantendo as rotas da API
]
