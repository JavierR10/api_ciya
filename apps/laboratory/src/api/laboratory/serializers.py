from rest_framework import serializers
from apps.laboratory.src.models.laboratory import Laboratory

class LaboratorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'