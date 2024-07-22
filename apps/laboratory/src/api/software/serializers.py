from rest_framework import serializers
from apps.laboratory.src.models.software import Software

class SoftwareSerializers(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'