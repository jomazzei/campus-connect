from .models import Event
from django import forms
from datetime import time


class CreateEventForm(forms.ModelForm):
    """
    Form to create event.
    Sets the fields that go to the database
    """
    class Meta:
        model = Event
        fields = ("title","content","venue","event_host_date","event_host_time","max_people","featured_image",)
        
        widgets = {
            'event_host_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        
        }