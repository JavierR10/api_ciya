from rest_framework import viewsets
#MODELOS
from apps.academic.src.models.associatedDocument import AssociatedDocument

#serializers
from apps.academic.src.api.associatedDocument.serializers import AssociatedDocumentSerializers

class AssociatedDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = AssociatedDocumentSerializers
    
    def get_queryset(self):
        return AssociatedDocument.objects.all()
