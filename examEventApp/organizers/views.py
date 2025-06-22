from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrganizerCreateForm
from django.utils import timezone

from .models import Organizer
from .forms import OrganizerEditForm
from events.models import Event



def organizer_create(request):
    if request.method == 'POST':
        form = OrganizerCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list')
    else:
        form = OrganizerCreateForm()
    return render(request, 'create-organizer.html', {'form': form})



def organizer_details(request):
    organizer = Organizer.objects.first()
    has_organizer = organizer is not None
    upcoming_events = []
    if organizer:
        upcoming_events = Event.objects.filter(
            organizer=organizer,
            start_time__gt=timezone.now()
        ).order_by('start_time')
    context = {
        'organizer': organizer,
        'has_organizer': has_organizer,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'details-organizer.html', context)

def organizer_edit(request):
    organizer = get_object_or_404(Organizer)
    if request.method == 'POST':
        form = OrganizerEditForm(request.POST, instance=organizer)
        if form.is_valid():
            form.save()
            return redirect('organizer_details')
    else:
        form = OrganizerEditForm(instance=organizer)
    return render(request, 'edit-organizer.html', {'form': form})


def organizer_delete(request):
    organizer = Organizer.objects.first()
    now = timezone.now()
    upcoming_events = Event.objects.filter(organizer=organizer, start_time__gt=now)

    if request.method == 'POST':
        if not upcoming_events.exists():
            # Delete all events first (cascade may also do it, but safe for logic)
            Event.objects.filter(organizer=organizer).delete()
            # Delete organizer
            organizer.delete()
        # Always redirect to index after POST
        return redirect('index')

    return render(request, 'delete-organizer.html')