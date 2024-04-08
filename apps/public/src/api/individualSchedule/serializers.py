from rest_framework import serializers
from apps.public.src.models.individualSchedule import IndividualSchedule

class IndividualScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndividualSchedule
        fields = '__all__'