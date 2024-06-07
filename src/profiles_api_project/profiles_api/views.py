from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ test api view """

    def get(self, request,format=None):

        an_apiview =[
        'uses HTTP methods as function (get,post,patch,put,delete)',
        'similar to traditional django view',
        'gives you most controle of your logic',
        'mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
