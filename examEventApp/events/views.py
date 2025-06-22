from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from events.forms import EventCreateForm
from events.models import Event
from organizers.models import Organizer



def events_list(request):
    events = Event.objects.all().order_by('-start_time')
    has_organizer = Organizer.objects.exists()
    return render(request, 'events.html', {'events': events, 'has_organizer': has_organizer})

def event_create(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = Organizer.objects.first()
            event.save()
            return redirect('events_list')
    else:
        form = EventCreateForm()
    return render(request, 'create-event.html', {'form': form})


def event_details(request, event_pk):
    event = Event.objects.get(pk=event_pk)
    has_organizer = Organizer.objects.exists()
    return render(request, 'details-event.html', {'event': event, 'has_organizer': has_organizer})



def event_edit(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    has_organizer = Organizer.objects.exists()
    if request.method == 'POST':
        form = EventCreateForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_details', event_pk=event.pk)
    else:
        form = EventCreateForm(instance=event)
    return render(request, 'edit-event.html', {
        'form': form,
        'event': event,
        'has_organizer': has_organizer
    })


def event_delete(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    has_organizer = Organizer.objects.exists()
    if request.method == 'POST':
        event.delete()
        return redirect('events_list')
    else:
        form = EventCreateForm(instance=event)
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True


    return render(request, 'delete-event.html', {
        'form': form,
        'event': event,
        'has_organizer': has_organizer,
    })