from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the forum app!")

def dashboard(request):
    context = {
        "first_name": "Vasil",
        "last_name": "Kichukov",
        "is_hungry": None,
        "favorite_songs": ["The song", "Lol"],
        "current_time": datetime.now()
    }
    print(reversed("dashboard"))

    return render(request, 'base.html', context)