from rest_framework import serializers
from apps.bonding.src.models.documentsVin import DocumentsVin

class DocumentsVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = DocumentsVin
        fields = '__all__'