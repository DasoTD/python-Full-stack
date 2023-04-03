from .views import main, RoomView
# from ..api.views import main, RoomView
from django.urls import path

urlpatterns = [
    path('', RoomView.as_view())
]