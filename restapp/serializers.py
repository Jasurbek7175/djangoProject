from rest_framework import serializers
from .models import FinanceModel, YoursDataModel
from rest_framework.decorators import api_view


class YourDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceModel
        # fields = '__all__'
        exclude = ['id', 'created_at']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoursDataModel
        exclude = ['id', 'created_at']
        # fields = ['name', 'age', 'city']

# @api_view(['POST'])
# def endpoint_api(request):
#     # Retrieve all objects from the YourDataModel model
#     queryset = YoursDataModel.objects.all()
#
#     # Serialize the queryset using YourDataModelSerializer
#     serializer = YourDataModelSerializer(queryset, many=True)
#     serialized_data = serializer.data
#
#     # Return the serialized data as JSON response
#     return Response(serialized_data)


from rest_framework import serializers
from .models import UploadedFile

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ('file', 'uploaded_on',)


