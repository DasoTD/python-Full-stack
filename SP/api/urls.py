from .views import main, RoomView, CreatePost,CreateRoom, CreateRoomView, signup, Signup
# from ..api.views import main, RoomView
from django.urls import path

urlpatterns = [
    path('', RoomView.as_view()),
    path('create-post', CreatePost.as_view()),
    path('create-room', CreateRoom.as_view()),
    path('auth', CreateRoomView.as_view()),
    path('signup', view=signup, name='signup'),
    path('Signup', Signup.as_view())
]