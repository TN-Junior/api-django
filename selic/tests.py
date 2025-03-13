from django.test import TestCase
from .models import SelicRate

class SelicRateTest(TestCase):
    def setUp(self):
        SelicRate.objects.create(data="2024-01-01", valor=10.5)

    def test_selic_rate(self):
        taxa = SelicRate.objects.get(data="2024-01-01")
        self.assertEqual(taxa.valor, 10.5)