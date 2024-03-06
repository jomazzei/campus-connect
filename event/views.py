from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Event
from django.contrib import messages
from .forms import CreateEventForm


# Create your views here.
class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "event_list.html"

def AboutPage(request):
    return render(
        request,
        "event/about.html",
    )


def create_event(request):
    if request.method == "POST":
        event_form = CreateEventForm(request.POST)
        if event_form.is_valid():
            print("SUCCESS")
            event = event_form.save(commit=False)
            event.organizer = request.user
            event.event_host_time = request.POST.get("event_time")
            event.save()
            messages.add_message(request, messages.SUCCESS, "You have created an event")
            return HttpResponseRedirect("success/")        
    else:
        event_form = CreateEventForm()
    # Needs another instance of form creation so it clears form on refresh/redirect
    return render(request, "event/form_create_event.html", {"event_form":event_form})

def create_success(request):
    return render(request, "event/form_create_success.html")