from rest_framework import serializers
from apps.public.src.models.security import Security

class SecuritySerializers(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'