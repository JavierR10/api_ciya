from rest_framework import serializers
from apps.bonding.src.models.groupVin import GroupVin

class GroupVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupVin
        fields = '__all__'