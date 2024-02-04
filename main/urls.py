from django.urls import path

from main.views import import_data, export_data

app_name = 'main'

urlpatterns = [
    path('import/', import_data),
    path('export/', export_data, name='export-data'),
]
