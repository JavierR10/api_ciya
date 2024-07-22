from rest_framework import serializers
from apps.public.src.models.profileUsers import profileUsers

class ProfileUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = profileUsers
        fields = '__all__'