from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from zip_codes_mx.models import PostalCode, Settlement, City
from zip_codes_mx.serializers import PostalCodeSerializer, CitySerializer, StateSerializer, SettlementSerializer
from zip_codes_mx.querys import city_name_search_engine

# ENDPOINT ELEMENTAL DE LA APP: busca por código postal.
class PostalCodeApi(APIView):

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



# ENDPOINT ELEMENTAL DE LA APP: busca por ciudad.
class CityApi(APIView):

    def get(self, request, format=None):
        return Response({'message': 'Hello, World!'})
    
    def post(self, request, format=None):
        
        # Recibir el nombre de la ciudad
        city_name = request.data.get('city')
        if not city_name:
            return Response({'error': 'Nombre de ciudad no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Realizar una consulta insensible a mayúsculas, minúsculas y acentos.
        city_rows = city_name_search_engine(city_name)
        if not city_rows:
            return Response({'error': 'Ciudad no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        # CREAR DICCIONARIO DE RESULTADOS
        results = []
        for city_row in city_rows:
            city_obj = City.objects.get(id=city_row[0])
            state_obj = city_obj.state
            postal_codes_obj = PostalCode.objects.filter(city=city_obj)

            serializer = {
                    "city": CitySerializer(city_obj).data.get('name'),
                    "state": StateSerializer(state_obj).data.get('name'),
                    "postal_codes": PostalCodeSerializer(postal_codes_obj, many=True).data
                }
            results.append(serializer)

        return Response(results, status=status.HTTP_200_OK)
