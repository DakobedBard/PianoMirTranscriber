from rest_framework import serializers
from upload.models import  DocumentFile


class DocumentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentFile
        fields = "__all__"

