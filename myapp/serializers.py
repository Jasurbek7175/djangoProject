from rest_framework import serializers
from .models import DataModel

class YourDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'