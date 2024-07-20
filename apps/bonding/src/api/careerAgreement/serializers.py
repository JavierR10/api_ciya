from rest_framework import serializers
from apps.bonding.src.models.careerAgreement import CareerAgreement

class CareerAgreementSerializers(serializers.ModelSerializer):
    class Meta:
        model = CareerAgreement
        fields = '__all__'