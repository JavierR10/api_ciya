from rest_framework import serializers
from apps.bonding.src.models.programVin import ProgramVin

class ProgramVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProgramVin
        fields = '__all__'