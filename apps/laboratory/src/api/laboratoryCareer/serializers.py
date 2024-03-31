from rest_framework import serializers
from apps.laboratory.src.models.laboratoryCareer import LaboratoryCareer

class LaboratoryCareerSerializers(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryCareer
        fields = '__all__'