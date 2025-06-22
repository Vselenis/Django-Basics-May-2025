from django.http import HttpResponse
from django.shortcuts import render

from organizers.models import Organizer


def index(request):
    return HttpResponse("Index page")


def index(request):
    has_organizer = Organizer.objects.exists()
    return render(request, 'index.html', {'has_organizer': has_organizer})