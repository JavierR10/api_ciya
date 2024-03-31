from rest_framework import viewsets
#MODELOS
from apps.public.src.models.teacher import Teacher

#serializers
from apps.public.src.api.teacher.serializers import TeacherSerializers

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializers
    
    def get_queryset(self):
        return Teacher.objects.filter(deleted_at__isnull=True)