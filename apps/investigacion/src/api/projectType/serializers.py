from rest_framework import serializers
from apps.investigacion.src.models.projectType import ProjectType

class ProjectTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'