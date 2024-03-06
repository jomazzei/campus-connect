from django.shortcuts import render
from django.views import generic
from .models import Event


# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "event_list.html"

def CreateForm(request):
    return render(
        request,
        "event/form_create_event.html",
    ) 

def AboutPage(request):
    return render(
        request,
        "event/about.html",
    )