from rest_framework import serializers
from apps.public.src.models.course import Course

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'