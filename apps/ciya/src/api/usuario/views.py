from rest_framework import viewsets
#MODELOS
from apps.ciya.src.models.usuario import users

#serializers
from apps.ciya.src.api.usuario.serializers import UsersSerializers

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializers
    
    def get_queryset(self):
        return users.objects.filter(deleted_at__isnull=True)