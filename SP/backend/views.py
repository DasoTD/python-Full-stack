from django.shortcuts import render
from django.http import HttpResponse
from requests import Response
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rum, Post
from .serializers import RoomSerializers, CreatePostSerializers, createRoomSerializer

# Create your views here.

def main(request):
    return HttpResponse('AWAYU')

class RoomView(generics.ListAPIView):
    queryset = Rum.objects.all()
    serializer_class = RoomSerializers

class CreateRoom(APIView):
    serializer_classc= createRoomSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_classc(data=request.data)
        if serializer.is_valid():
            votes_to_skip = serializer.data.get('votes_to_skip')
            guest_can_pause = serializer.data.get('guest_can_pause')
            host = self.request.session.session_key
            queryset = Rum.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.votes_to_skip = votes_to_skip
                room.guest_can_pause = guest_can_pause
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
            else:
                room = Rum(host=host, votes_to_skip=votes_to_skip,guest_can_pause=guest_can_pause)
                room.save()
            return Response(RoomSerializers(room).data, status=status.HTTP_201_CREATED)

class CreatePost(APIView):
    serializer_class = CreatePostSerializers
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # user', 'image', 'caption', 'created_at', 'no_of_likes
            user = serializer.data.get('user')
            image = serializer.data.get('image')
            caption = serializer.data.get('caption')
            post = Post(user=user,image=image,caption=caption)
            post.save()

        return Response(RoomView(post).data, status=status.HTTP_201_CREATED)
