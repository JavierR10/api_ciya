from rest_framework import serializers
from apps.bonding.src.models.registrationVin import RegistrationVin

class RegistrationVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistrationVin
        fields = '__all__'