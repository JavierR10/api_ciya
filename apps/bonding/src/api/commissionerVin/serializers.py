from rest_framework import serializers
from apps.bonding.src.models.commissionerVin import CommissionerVin

class CommissionerVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommissionerVin
        fields = '__all__'