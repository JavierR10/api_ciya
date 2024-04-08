from rest_framework import serializers
from apps.bonding.src.models.type import Type

class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'