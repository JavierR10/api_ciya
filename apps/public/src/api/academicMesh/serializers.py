from rest_framework import serializers
from apps.public.src.models.academicMesh import AcademicMesh

class AcademicMeshSerializers(serializers.ModelSerializer):
    class Meta:
        model = AcademicMesh
        fields = '__all__'