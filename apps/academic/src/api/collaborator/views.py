from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.academic.src.api.globalFilter.filter.filters import NewsFilterCollaborator
#MODELOS
from apps.academic.src.models.collaborator import Collaborator

#serializers
from apps.academic.src.api.collaborator.serializers import CollaboratorSerializers

class CollaboratorViewSet(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializers
    queryset = Collaborator.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCollaborator
    pagination_class = CustomPagination

