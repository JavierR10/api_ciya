from rest_framework import serializers
from apps.investigacion.src.models.equipment import Equipment

class EquipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'