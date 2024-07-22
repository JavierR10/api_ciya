from rest_framework import serializers
from apps.public.src.models.distributive import Distributive

class DistributiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Distributive
        fields = '__all__'