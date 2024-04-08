from rest_framework import serializers
from apps.public.src.models.counter import Counter

class CounterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'