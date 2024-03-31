from rest_framework import serializers
from apps.investigacion.src.models.sublinea import Sublinea

class SublineaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sublinea
        fields = '__all__'