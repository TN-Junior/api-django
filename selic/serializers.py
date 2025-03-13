from rest_framework import serializers
from .models import SelicRate

class SelicRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelicRate
        fields = '__all__'
