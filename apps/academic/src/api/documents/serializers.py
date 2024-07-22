from rest_framework import serializers
from apps.academic.src.models.documents import Documents

class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'