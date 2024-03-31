from rest_framework import serializers
from apps.laboratory.src.models.reservationType import ReservationType

class ReservationTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReservationType
        fields = '__all__'