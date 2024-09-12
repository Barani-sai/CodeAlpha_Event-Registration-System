from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from django.utils import timezone
from .forms import EventForm
from .models import Event

# View for listing all upcoming events
def event_list(request):
    # Fetch all events that are happening in the future
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

# View for showing details of a specific event
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Check if the user is already registered for the event
    is_registered = Registration.objects.filter(event=event, user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'events/event_detail.html', {'event': event, 'is_registered': is_registered})

# View for registering a user for an event
@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Check if the user is already registered
    if Registration.objects.filter(event=event, user=request.user).exists():
        return render(request, 'events/registration_error.html', {'message': 'You are already registered for this event.'})
    
    # Check if the event has reached its max capacity
    if Registration.objects.filter(event=event).count() >= event.max_attendees:
        return render(request, 'events/registration_error.html', {'message': 'This event has reached its maximum capacity.'})

    # Register the user for the event
    Registration.objects.create(event=event, user=request.user)
    return redirect('event_detail', event_id=event.id)

# View for displaying the user's registrations
@login_required
def user_registrations(request):
    # Fetch all registrations for the logged-in user
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/user_registrations.html', {'registrations': registrations})

# View for canceling a user's registration for an event
@login_required
def cancel_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registration = get_object_or_404(Registration, event=event, user=request.user)
    
    # Delete the registration
    registration.delete()
    return redirect('user_registrations')

from django.shortcuts import render
from .models import Event

def main_page(request):
    events = Event.objects.all()
    return render(request, 'events/main_page.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')  # Redirect to the main page after saving
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})
