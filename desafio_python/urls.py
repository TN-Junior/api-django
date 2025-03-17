from django.urls import path, include
from rest_framework.routers import DefaultRouter
from selic.views import SelicRateViewSet, index  # Importando a função index corretamente
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'selic', SelicRateViewSet, basename='selic')  # Definindo o basename 

urlpatterns = [
    path('', index, name='index'),  # Certificando-se de que 'index' existe no views.py
    path('api/', include(router.urls)),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Gera access e refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Atualiza access token
]
