from django.urls import path
from .views import upload_file, success, create_excel_file, Data, YourDataModelAPIView, DataModelAPIView

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('success/', success, name='success'),
    path('create_excel/', create_excel_file, name='create_excel_file'),
    path('json/', Data.as_view(), name='create_append'),
    # path('endpoint/', YourDataModelAPIView.as_view(), name='your-data-api'),
    path('endpoint/', YourDataModelAPIView.as_view(), name='your-data-api'),
]