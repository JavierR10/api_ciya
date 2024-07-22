from rest_framework import serializers
from apps.bonding.src.models.documets import Documents

class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'