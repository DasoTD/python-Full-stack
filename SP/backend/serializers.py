from rest_framework import serializers
from .models import Rum

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model= Rum
        fields= '__all__' #('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip')