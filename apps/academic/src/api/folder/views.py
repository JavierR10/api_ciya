from rest_framework import viewsets
#MODELOS
from apps.academic.src.models.folder import Folder

#serializers
from apps.academic.src.api.folder.serializers import FolderSerializers

class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = FolderSerializers
    
    def get_queryset(self):
        return Folder.objects.all()
