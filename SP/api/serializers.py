from rest_framework import serializers
from .models import Rum, Post, UserProfile

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model= Rum
        fields= '__all__' #('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip')
class createRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rum
        fields=('guest_can_pause', 'votes_to_skip')

class Signup(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('firstname', 'lastname', 'username', 'email', 'password', 'phone_number')

        
class CreatePostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= ('user', 'image', 'caption') #'__all__'