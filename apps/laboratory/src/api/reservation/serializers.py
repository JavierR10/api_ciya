from rest_framework import serializers
from apps.laboratory.src.models.reservation import Reservation

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'