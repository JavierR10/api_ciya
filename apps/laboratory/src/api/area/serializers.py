from rest_framework import serializers
from apps.laboratory.src.models.area import Area

class AreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'