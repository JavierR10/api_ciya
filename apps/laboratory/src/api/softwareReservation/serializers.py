from rest_framework import serializers
from apps.laboratory.src.models.softwareReservation import SoftwareReservation

class SoftwareReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = SoftwareReservation
        fields = '__all__'