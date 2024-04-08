from rest_framework import serializers
from apps.public.src.models.students import Students

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'