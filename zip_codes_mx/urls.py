from django.urls import path
from zip_codes_mx import api

urlpatterns = [
    path('zip_api/', api.ZipApi.as_view(), name='zip_api'),
]