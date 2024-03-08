from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .models import Event
from django.contrib import messages
from .forms import CreateEventForm
from datetime import datetime

from django.views.generic.edit import CreateView


# Sets Home page
def home_page(request):
    return render(
        request,
        "event/index.html"
    )


# Sets About page
def AboutPage(request):
    return render(
        request,
        "event/about.html",
    )


# List view for all Event items
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.all()
    template_name = "event_list.html"
    paginate_by = 9


# View for individual event pages
def event_detail(request, slug):
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "event/event_detail.html",
        {
            "event": event
        }
    )


# View to handle the Create Event page
def create_event(request):

    if request.method == "POST":
        event_form = CreateEventForm(request.POST)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.organizer = request.user
            try:
                event.save()
                messages.success(request, "You have created an event")
                return redirect("success/")
                
            except ValueError:
                messages.error(request, "Invalid time format. Please use Hour:Minute:Second format. f.e. 10:00:00")

    else:
        event_form = CreateEventForm()

    return render(request, "event/form_create_event.html", {"event_form":event_form})


# The page that the user is redirected to on valid form submission
def create_success(request):
    return render(request, "event/form_create_success.html")


# Attend Event view
def attend_event(request, slug):
    event = Event.objects.get(slug=slug)
    # check if the event is still available
    if event.attendance_count < event.max_people:
        # check if user is already attending
        if str(request.user) not in str(event.attendance_list):
            event.attendance_count = event.attendance_count + 1
            event.attendance_list = str(event.attendance_list) + " " + str(request.user)
            event.save()
    return HttpResponseRedirect(reverse('event_detail', args=[slug]))

def delete_event(request, slug):
    event = Event.objects.get(slug=slug)
    if request.user == event.organizer:
        event.delete()
    return HttpResponseRedirect(reverse('event-list'))