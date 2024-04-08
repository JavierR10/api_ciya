from rest_framework import serializers
from apps.bonding.src.models.agreement import Agreement

class AgreementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'