from rest_framework import serializers
from apps.academic.src.models.collaborator import Collaborator

class CollaboratorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'