from rest_framework import serializers
from apps.investigacion.src.models.paisSv import PaisSv

class PaisSvSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaisSv
        fields = '__all__'