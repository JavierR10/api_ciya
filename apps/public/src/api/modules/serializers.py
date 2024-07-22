from rest_framework import serializers
from apps.public.src.models.modules import Module

class ModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'