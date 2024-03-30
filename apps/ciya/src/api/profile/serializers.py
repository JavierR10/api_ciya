from rest_framework import serializers
from apps.ciya.src.models.profile import profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'