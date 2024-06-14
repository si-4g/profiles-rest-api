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
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileFeedItemSerilizer(serializers.ModelSerializer):
    """a serilizer for profile feed item"""
    class Meta:
        model=models.ProfileFeedItem
        fields= ('id','user_profile','status_text','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}
