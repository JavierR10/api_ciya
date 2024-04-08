from rest_framework import serializers
from apps.bonding.src.models.process import Process

class ProcessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'