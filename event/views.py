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
            event_form.save(commit=False)
            event_form.event_host_time = request.POST.get("event_time")
            event_form.save()
            messages.add_message(request, messages.SUCCESS, "You have created an event")
            return HttpResponseRedirect(request.path_info)
    else:
        event_form = CreateEventForm()
    return render(request, "event/form_create_event.html", {"event_form":event_form})