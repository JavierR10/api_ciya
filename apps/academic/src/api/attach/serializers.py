from rest_framework import serializers
from apps.academic.src.models.attach import Attach

class AttachSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attach
        fields = '__all__'