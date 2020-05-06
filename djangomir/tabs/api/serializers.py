from rest_framework import serializers
from tabs.models import GuitarTab

class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuitarTab
        fields = ['id', 'name','notes']

