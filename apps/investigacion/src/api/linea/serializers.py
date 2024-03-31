from rest_framework import serializers
from apps.investigacion.src.models.linea import Linea

class LineaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = '__all__'