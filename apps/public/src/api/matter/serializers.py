from rest_framework import serializers
from apps.public.src.models.matter import Matter

class MatterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Matter
        fields = '__all__'