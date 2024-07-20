from rest_framework import serializers
from apps.bonding.src.models.scheduleVin import ScheduleVin

class ScheduleVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScheduleVin
        fields = '__all__'