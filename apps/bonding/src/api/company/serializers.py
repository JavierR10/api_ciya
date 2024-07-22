from rest_framework import serializers
from apps.bonding.src.models.company import Company

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'