from rest_framework import viewsets
#MODELOS
from apps.academic.src.models.documents import Documents

#serializers
from apps.academic.src.api.documents.serializers import DocumentsSerializers

class DocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentsSerializers
    
    def get_queryset(self):
        return Documents.objects.filter(deleted_at__isnull=True)
