from rest_framework import serializers
from apps.ciya.src.models.profileUsers import profileUsers

class ProfileUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = profileUsers
        fields = '__all__'