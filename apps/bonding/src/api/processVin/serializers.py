from rest_framework import serializers
from apps.bonding.src.models.processVin import ProcessVin

class ProcessVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProcessVin
        fields = '__all__'