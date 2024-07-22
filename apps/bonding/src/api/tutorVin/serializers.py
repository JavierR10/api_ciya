from rest_framework import serializers
from apps.bonding.src.models.tutorVin import TutorVin

class TutorVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = TutorVin
        fields = '__all__'