from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import YourDataModel
import pandas as pd


def handle_uploaded_file(file):
    df = pd.read_excel(file)
    for index, row in df.iterrows():
        YourDataModel.objects.create(
            name=row['Name'],
            age=row['Age'],
            city=row['City'],
            # Add more fields as needed
        )


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})


def success(request):
    # Add any success message or redirection logic here
    return render(request, 'success.html')


from django.http import HttpResponse
import pandas as pd
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def create_excel_file(request):
    # Your data retrieval logic goes here
    data = {
        'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 22],
        'City': ['New York', 'London', 'Paris'],
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Create a response object with the appropriate content type for Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=my_project_data.xlsx'

    # Write the DataFrame to the response object
    df.to_excel(response, index=False, engine='openpyxl')

    return response

import requests
from rest_framework.views import APIView

class Data(APIView):
    def post(request):
        data = YourDataModel.objects.all()

        df = pd.DataFrame(data)

        columns_to_exclude = ['id']
        df = df.loc[:, (df != 0).any(axis=0) & ~df.columns.isin(columns_to_exclude)]

        # Convert the DataFrame to JSON format
        json_data = df.to_json(orient='records')

        # Parse the JSON data to a Python list
        parsed_data = json.loads(json_data)

        # Append the new object to the array
        # new_object = {'Name': 'Alice', 'Age': 28, 'City': 'Berlin'}
        # parsed_data.append(new_object)

        # Convert the updated array back to JSON
        updated_json_data = json.dumps(parsed_data)

        api_url = 'http://127.0.0.1:8000/endpoint/'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(api_url, data=updated_json_data, headers=headers)

        if response.status_code == 201:
            return JsonResponse({'status': 'Data successfully sent to the API'})
        else:
            return JsonResponse({'status': 'Failed to send data to the API'}, status=500)

    # For simplicity, returning the JSON as a response in this example
    # return JsonResponse({'updated_data': updated_json_data, 'data': json_data})


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import YourDataModel
from .serializers import YourDataModelSerializer

class YourDataModelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = YourDataModelSerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .models import YourDataModel
from .serializers import YourDataModelSerializer

class DataModelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save objects for each item in the array
        for item in data:
            serializer = YourDataModelSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': 'Data successfully saved'}, status=status.HTTP_201_CREATED)




from django.db.models.signals import post_save
from django.dispatch import receiver
import requests

from .models import YourDataModel

@receiver(post_save, sender=YourDataModel)
def send_data_to_api(sender, instance, **kwargs):
    api_url = 'http://127.0.0.1:8000/endpoint/'  # Replace with your actual API endpoint
    headers = {'Content-Type': 'application/json'}

    # data_to_send = {
    #     "Name": instance.name,
    #     "Age": instance.age,
    #     "City": instance.city,
    # }

    data = YourDataModel.objects.all()

    df = pd.DataFrame(data)

    columns_to_exclude = ['id']
    df = df.loc[:, (df != 0).any(axis=0) & ~df.columns.isin(columns_to_exclude)]

    # Convert the DataFrame to JSON format
    json_data = df.to_json(orient='records')

    # Parse the JSON data to a Python list
    parsed_data = json.loads(json_data)

    # Append the new object to the array
    # new_object = {'Name': 'Alice', 'Age': 28, 'City': 'Berlin'}
    # parsed_data.append(new_object)

    # Convert the updated array back to JSON
    updated_json_data = json.dumps(parsed_data)


    try:
        response = requests.post(api_url, json=updated_json_data, headers=headers)

        if response.status_code == 201:
            print('Data successfully sent to the API')
        else:
            print(f'Failed to send data to the API. Response code: {response.status_code}')

    except requests.RequestException as e:
        print(f'Error during request: {str(e)}')



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import YourDataModel
from .serializers import YourDataModelSerializer

class ModelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save objects for each item in the array
        for item in data:
            serializer = YourDataModelSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': 'Data successfully saved'}, status=status.HTTP_201_CREATED)