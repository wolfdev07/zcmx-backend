# serializers.py
from rest_framework import serializers
from zip_codes_mx.models import State, City, PostalCode, Settlement, Municipality


class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = ['code']



class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = ['name', 'settlement_type']


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
