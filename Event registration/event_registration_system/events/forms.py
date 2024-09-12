from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description', 'max_attendees']  # Include max_attendees field
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
