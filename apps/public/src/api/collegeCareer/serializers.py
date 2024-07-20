from rest_framework import serializers
from apps.public.src.models.collegeCareer import CollegeCareer

class CollegeCareerSerializers(serializers.ModelSerializer):
    class Meta:
        model = CollegeCareer
        fields = '__all__'