from rest_framework import serializers
from apps.laboratory.src.models.laboratorySoftware import LaboratorySoftware

class LaboratorySoftwareSerializers(serializers.ModelSerializer):
    class Meta:
        model = LaboratorySoftware
        fields = '__all__'