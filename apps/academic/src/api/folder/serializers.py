from rest_framework import serializers
from apps.academic.src.models.folder import Folder

class FolderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'