from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.conf import settings
from zip_codes_mx.models import State

class ZipApi(APIView):

    def get(self, request, format=None):
        states = State.objects.all()
        print(states)
        return Response({'message': 'Hello, World!'})

    def post(self, request, format=None):
        return Response({'message': 'Hello, World!'})