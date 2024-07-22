from rest_framework import serializers
from apps.academic.src.models.news import News

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'