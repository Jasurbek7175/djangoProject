from django.urls import path
from .views import upload_file, success, create_excel_file,  YourDataModelAPIView, post_data,  get_objects_in_month, import_from_excel, FileUploadAPIView, uploadpdf, download_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('success/', success, name='success'),
    path('create_excel/', create_excel_file, name='create_excel_file'),
    # path('json/', Data.as_view, name='create_append'),
    # path('endpoint/', YourDataModelAPIView.as_view(), name='your-data-api'),
    path('endpoint/', YourDataModelAPIView.as_view(), name='your-data-api'),
    path('end/', post_data, name='your-api'),
    # path('endpoint-api/', data_send, name='yourapi'),
    path('monthly-data/', get_objects_in_month, name='api'),
    path('import/', import_from_excel, name='import_from_excel'),
    path('upload-file/', FileUploadAPIView.as_view(), name='upload-file'),
    path('uploadfile/', uploadpdf),
    path('download/<str:file_id>/', download_file, name='download_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
