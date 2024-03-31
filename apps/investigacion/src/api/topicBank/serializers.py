from rest_framework import serializers
from apps.investigacion.src.models.topicBank import TopicBank

class TopicBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = TopicBank
        fields = '__all__'