from .views import main, RoomView, CreatePost,CreateRoom
# from ..api.views import main, RoomView
from django.urls import path

urlpatterns = [
    path('', RoomView.as_view()),
    path('createPost', CreatePost.as_view()),
    path('createRoom', CreateRoom.as_view())
]