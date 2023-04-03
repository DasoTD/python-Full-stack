from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .models import Rum
from .serializers import RoomSerializers

# Create your views here.

def main(request):
    return HttpResponse('AWAYU')

class RoomView(generics.ListCreateAPIView):
    queryset = Rum.objects.all()
    serializer_class = RoomSerializers

class CreateRoom(APIView):
    pass
