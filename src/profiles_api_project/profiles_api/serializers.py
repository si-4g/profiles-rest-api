from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)



class UserProfilSerilizer(serializers.ModelSerializer):
    """a serilizer for our user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password': {'write_only':True} }

        def create(self,validated_data):
            """creates and return a new user"""
            user = models.UserProfile(
                emai=validated_data['email'],
                name = validated_data['name']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user