from rest_framework import serializers
from apps.laboratory.src.models.practicalGuide import PracticalGuide

class PracticalGuideSerializers(serializers.ModelSerializer):
    class Meta:
        model = PracticalGuide
        fields = '__all__'