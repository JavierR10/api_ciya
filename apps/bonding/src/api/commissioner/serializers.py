from rest_framework import serializers
from apps.bonding.src.models.commissioner import Commissioner

class CommissionerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Commissioner
        fields = '__all__'