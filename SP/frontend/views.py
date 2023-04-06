from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    # /home/david/Desktop/Music/SP/frontend/static/frontend
    return render(request, "frontend/index.html")