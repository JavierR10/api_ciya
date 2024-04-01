from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.group import Group

#serializers
from apps.investigacion.src.api.group.serializers import GroupSerializers

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializers
    
    def get_queryset(self):
        return Group.objects.all()
