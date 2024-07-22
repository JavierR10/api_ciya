from rest_framework import serializers
from apps.investigacion.src.models.project import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'