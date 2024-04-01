from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.project import Project

#serializers
from apps.investigacion.src.api.project.serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializers
    
    def get_queryset(self):
        return Project.objects.all()
