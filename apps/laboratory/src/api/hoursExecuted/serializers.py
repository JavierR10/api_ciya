from rest_framework import serializers
from apps.laboratory.src.models.hoursExecuted import HoursExecuted

class HoursExecutedSerializers(serializers.ModelSerializer):
    class Meta:
        model = HoursExecuted
        fields = '__all__'