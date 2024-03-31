from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.hoursExecuted import HoursExecuted

#serializers
from apps.laboratory.src.api.hoursExecuted.serializers import HoursExecutedSerializers

class HoursExecutedViewSet(viewsets.ModelViewSet):
    serializer_class = HoursExecutedSerializers
    
    def get_queryset(self):
        return HoursExecuted.objects.filter(deleted_at__isnull=True)
