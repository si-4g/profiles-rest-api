from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """ test api view """
    serializer_class = serializers.HelloSerializer
    def get(self, request,format=None):

        an_apiview =[
        'uses HTTP methods as function (get,post,patch,put,delete)',
        'similar to traditional django view',
        'gives you most controle of your logic',
        'mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
        """create a hellow message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')

            message = 'Hellow {0}'.format(name)

            return Response({'message': message})
        else :
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,resquest,pk=None):
        """handels updating an opject"""
        return Response({'method':'put'})

    def patch(self,resquest,pk=None):
        """patch request, only updates the fields provided in the request"""
        return Response({'method': 'patch'})


    def delete(self, resquest, pk=None):
        """deletes an opject"""
        return Response({'method': 'deldete'})



