from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.topicBank import TopicBank

#serializers
from apps.investigacion.src.api.topicBank.serializers import TopicBankSerializers

class TopicBankViewSet(viewsets.ModelViewSet):
    serializer_class = TopicBankSerializers
    
    def get_queryset(self):
        return TopicBank.objects.all()
