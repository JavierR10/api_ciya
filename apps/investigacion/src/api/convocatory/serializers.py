from rest_framework import serializers
from apps.investigacion.src.models.convocatory import Convocatory

class ConvocatorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Convocatory
        fields = '__all__'