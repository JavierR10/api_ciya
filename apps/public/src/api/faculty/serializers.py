from rest_framework import serializers
from apps.public.src.models.faculty import Faculty

class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'