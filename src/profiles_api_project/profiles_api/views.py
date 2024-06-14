from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

from . import models

from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import  IsAuthenticated
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
        """deletes an object"""
        return Response({'method': 'deldete'})



class HelloViewsets(viewsets.ViewSet):
    """test API ViewSet """

    serializer_class =  serializers.HelloSerializer

    def list(self,request):
        """return a hello message

        """

        a_viewset = [
            'uses actions (list, create , retrieve, update ,partial_update)',
            'automatically maps to URLs using routers',
            'provides more functionality with less code ',
        ]
        return Response({'message ':'hello ','a_viewset': a_viewset})

    def create(self,request):
        """creates a hello message"""

        serializer = serializers.HelloSerializer(data= request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else :
            return Response(
                serializer.errors,status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        """handels getting an object by its ID"""
        return Response({'http_method':'GET'})
    def update(self,request,pk=None):
        """handels updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """handels updating part of an object"""
        return Response({'http_method':'PATCH'})


    def destroy(self,request,pk=None):
        """handels removing an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """handels creating and updating profiles"""

    serializer_class = serializers.UserProfilSerilizer
    queryset =models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewset(viewsets.ViewSet):
    """checks email and password and return an auth token"""
    serializer_class = AuthTokenSerializer
    def create(self, request):
        """use the ObtainAuthToken APIView to validate and creat a token"""
        return ObtainAuthToken().post(request)


class UserProfileFeedViewset(viewsets.ModelViewSet):
    """handels creating reading and updating profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerilizer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged-in user"""
        serializer.save(user_profile=self.request.user)
