# serializers.py
from rest_framework import serializers
from zip_codes_mx.models import State, City, PostalCode, Settlement


class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = '__all__'



class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = ['name', 'settlement_type']



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
