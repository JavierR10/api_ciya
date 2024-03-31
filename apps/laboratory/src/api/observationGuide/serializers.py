from rest_framework import serializers
from apps.laboratory.src.models.observationGuide import ObservationGuide

class ObservationGuideSerializers(serializers.ModelSerializer):
    class Meta:
        model = ObservationGuide
        fields = '__all__'