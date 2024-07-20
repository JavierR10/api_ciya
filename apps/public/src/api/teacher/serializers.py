from rest_framework import serializers
from apps.public.src.models.teacher import Teacher

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'