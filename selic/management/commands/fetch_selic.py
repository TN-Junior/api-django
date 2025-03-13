import requests
from django.core.management.base import BaseCommand
from selic.models import SelicRate
from datetime import datetime

class Command(BaseCommand):
    help = 'Importa as taxas Selic da API do Banco Central'

    def handle(self, *args, **kwargs):
        url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json"
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            for item in dados:
                data_formatada = datetime.strptime(item['data'], '%d/%m/%Y').date()
                taxa_valor = float(item['valor'])

                # Verifica se a taxa já existe para essa data
                if not SelicRate.objects.filter(data=data_formatada).exists():
                    SelicRate.objects.create(data=data_formatada, valor=taxa_valor)
                    self.stdout.write(self.style.SUCCESS(f'Taxa {taxa_valor}% adicionada para {data_formatada}'))
        else:
            self.stdout.write(self.style.ERROR("Erro ao buscar os dados da API!"))
