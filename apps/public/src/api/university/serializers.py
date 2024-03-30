from rest_framework import serializers
from apps.public.src.models.university import universidad

class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = universidad
        fields = '__all__'