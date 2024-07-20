from rest_framework import serializers
from apps.public.src.models.period import Period

class PeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'