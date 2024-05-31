from django.urls import path
from zip_codes_mx import api

urlpatterns = [
    path('postal-code/', api.PostalCodeApi.as_view(), name='postal_code_api'),
    path('city/', api.CityApi.as_view(), name='city_api'),
]