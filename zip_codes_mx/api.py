from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from zip_codes_mx.models import PostalCode, Settlement
from zip_codes_mx.serializers import PostalCodeSerializer, CitySerializer, StateSerializer, SettlementSerializer


# ENDPOINT ELEMENTAL DE LA APP
class ZipApi(APIView):

    def get(self, request, format=None):

        return Response({'message': 'Hello, World!'})

    def post(self, request, format=None):

        postal_code = request.data.get('postal_code')
        
        try:
            postal_code_obj = PostalCode.objects.get(code=postal_code)
            settlements_obj = Settlement.objects.filter(postal_code=postal_code_obj)
            city_obj = postal_code_obj.city
            state_obj = city_obj.state
            
            serializer = {
                "postal_code": PostalCodeSerializer(postal_code_obj).data.get('code'),
                "city": CitySerializer(city_obj).data.get('name'),
                "state": StateSerializer(state_obj).data.get('name'),
                "settlements": SettlementSerializer(settlements_obj, many=True).data
            }
            return Response(serializer, status=status.HTTP_200_OK)
        
        except PostalCode.DoesNotExist:
            return Response({'error': 'Código Postal no encontrado'}, status=status.HTTP_404_NOT_FOUND)