from rest_framework import serializers
from apps.public.src.models.studentRepresentatives import StudentRepresentatives

class StudentRepresentativesSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentRepresentatives
        fields = '__all__'