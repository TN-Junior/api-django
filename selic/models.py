from django.db import models

class SelicRate(models.Model):
    data = models.DateField(unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Aumentado para evitar erro

    def __str__(self):
        return f"{self.data} - {self.valor}%"