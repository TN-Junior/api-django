from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from selic.models import SelicRate
from datetime import date

class SelicRateAPITest(APITestCase):
    def setUp(self):
        """Configura um usuário e um registro de teste"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.selic = SelicRate.objects.create(data=date(2024, 1, 1), valor=10.5)
        self.api_url = "/api/selic/"  # URL da API

    def test_get_selic_rates(self):
        """Verifica se a API retorna a lista de taxas"""
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.json()), 0)  # Deve retornar pelo menos um item

    def test_create_selic_rate_unauthorized(self):
        """Testa se um usuário não autenticado não pode criar taxa"""
        response = self.client.post(self.api_url, {"data": "2024-02-01", "valor": 11.0})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Deve falhar

    def test_create_selic_rate_authorized(self):
        """Testa a criação de taxa Selic com usuário autenticado"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(self.api_url, {"data": "2024-02-01", "valor": 11.0})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_selic_rate(self):
        """Testa a exclusão de uma taxa existente"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(f"{self.api_url}{self.selic.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
