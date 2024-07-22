from rest_framework import serializers
from apps.bonding.src.models.typeVin import TypeVin

class TypeVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeVin
        fields = '__all__'