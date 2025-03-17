from django.test import TestCase
from django.db.utils import IntegrityError
from selic.models import SelicRate
from datetime import date
from decimal import Decimal

class SelicRateModelTest(TestCase):
    def setUp(self):
        """Criação de um registro inicial"""
        self.selic = SelicRate.objects.create(data=date(2024, 1, 1), valor=Decimal("10.50"))  # Mantém precisão

    def test_selic_creation(self):
        """Testa se a taxa Selic foi corretamente criada"""
        self.assertEqual(self.selic.valor, Decimal("10.50"))  # Garante precisão do DecimalField
        self.assertEqual(self.selic.data, date(2024, 1, 1))

    def test_unique_date_constraint(self):
        """Verifica se duas taxas não podem ter a mesma data"""
        with self.assertRaises(IntegrityError):
            SelicRate.objects.create(data=date(2024, 1, 1), valor=Decimal("11.00"))  # Testa outro valor

    def test_string_representation(self):
        """Verifica o retorno da string no modelo"""
        self.assertEqual(str(self.selic), "2024-01-01 - 10.50%")  # Formato correto com duas casas decimais
