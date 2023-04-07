from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from requests import Response
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rum, Post, UserProfile
from .serializers import RoomSerializers, CreatePostSerializers, createRoomSerializer, Signup
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,  auth
from django.contrib.auth import authenticate
# from rest_framework.authentication import authenticate
# from .models import FollowerCount, Profile, Post, likePost, FollowerCount
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging
from django.views.decorators.csrf import csrf_exempt
import environ
env = environ.Env(DEBUG=(bool, False))
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
    

class CreateRoomView(APIView):
    serializer_class = createRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Rum.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializers(room).data, status=status.HTTP_200_OK)
            else:
                room = Rum(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                return Response(RoomSerializers(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class Signup(APIView):
    serializer_class = Signup
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        password1 = request.data.get('password')
        password2 = request.data.get('password2')
        if not password1 == password2:
            messages.info(request,'password did not match')
            # return redirect('/signup')
            return Response({'wahala Request': 'Password did not match...'})
        if serializer.is_valid():
            username = serializer.data.get('username')
            lastname = serializer.data.get('lastname')
            firstname = serializer.data.get('firstname')
            email = serializer.data.get('email')
            phone_number = serializer.data.get('phone_number')
            password = serializer.data.get('password')
            password = make_password(password, salt=env("SALT"), hasher='default')
            if UserProfile.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return Response({'wahala Request': 'email already exist...'})
            if UserProfile.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return Response({'wahala Request': 'username already exist...'})
            if UserProfile.objects.filter(phone_number=phone_number).exists():
                messages.info(request,'number already exist')
                return Response({'wahala Request': 'number already exist...'})
            else:
                profile = UserProfile(username=username, lastname=lastname, firstname=firstname,email=email,phone_number=phone_number, password=password)
                profile.save()
                return Response({'Good Request': 'valid data...'}, status=status.HTTP_201_CREATED)
            
            
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(username, email, username)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                user_model = User.objects.get(username=username)
                new_profile= UserProfile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('/setting')
        else:
            messages.info(request, 'password not match')
            return redirect('/signup') 
    else:
        return render(request, 'signup.html')
