from rest_framework import serializers
from apps.public.src.models.careerArea import CareerArea

class CareerAreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CareerArea
        fields = '__all__'