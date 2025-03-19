from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from selic.models import SelicRate
from datetime import date

class SelicPermissionsTest(APITestCase):
    def setUp(self):
        """Criação de usuário normal e superusuário"""
        self.normal_user = User.objects.create_user(username="normal", password="123")
        self.admin_user = User.objects.create_superuser(username="admin", password="adminpass")
        self.selic = SelicRate.objects.create(data=date(2024, 1, 1), valor=10.5)
        self.api_url = f"/api/selic/{self.selic.id}/"

    def test_normal_user_cannot_delete(self):
        """Usuário normal não pode deletar"""
        self.client.force_authenticate(user=self.normal_user)  # 🔹 Corrigindo a autenticação
        response = self.client.delete(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_user_can_delete(self):
        """Superusuário pode deletar"""
        self.client.force_authenticate(user=self.admin_user)  # 🔹 Corrigindo a autenticação
        response = self.client.delete(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
