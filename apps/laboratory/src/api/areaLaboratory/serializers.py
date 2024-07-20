from rest_framework import serializers
from apps.laboratory.src.models.areaLaboratory import AreaLaboratory

class AreaLaboratorySerializers(serializers.ModelSerializer):
    class Meta:
        model = AreaLaboratory
        fields = '__all__'