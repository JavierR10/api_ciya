from rest_framework import serializers
from apps.ciya.src.models.usuario import users

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'