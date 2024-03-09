from django.urls import path

from main.views import import_data, export_data, web_hook_view

app_name = 'main'

urlpatterns = [
    path('import/', import_data),
    path('export/', export_data, name='export-data'),
    path('webhook/', web_hook_view, name='webhook'),
]
