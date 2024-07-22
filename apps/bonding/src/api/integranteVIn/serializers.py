from rest_framework import serializers
from apps.bonding.src.models.integranteVIn import IntegranteVin

class IntegranteVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = IntegranteVin
        fields = '__all__'