from rest_framework import serializers
from apps.bonding.src.models.projectVin import ProjectVin

class ProjectVinSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectVin
        fields = '__all__'