from rest_framework import serializers
from apps.investigacion.src.models.group import Group

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'