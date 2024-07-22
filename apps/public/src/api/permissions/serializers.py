from rest_framework import serializers
from apps.public.src.models.permissions import Permissions

class PermissionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'