from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.projectType import ProjectType

#serializers
from apps.investigacion.src.api.projectType.serializers import ProjectTypeSerializers

class ProjectTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTypeSerializers
    
    def get_queryset(self):
        return ProjectType.objects.filter(deleted_at__isnull=True)
