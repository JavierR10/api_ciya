from rest_framework import serializers
from apps.academic.src.models.associatedDocument import AssociatedDocument

class AssociatedDocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AssociatedDocument
        fields = '__all__'