from rest_framework import serializers
from apps.investigacion.src.models.paisBm import PaisBm

class PaisBmSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaisBm
        fields = '__all__'