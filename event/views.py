from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Event
from django.contrib import messages
from .forms import CreateEventForm
from datetime import datetime



# Create your views here.

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
    queryset = Event.objects.all()
    template_name = "event_list.html"


# View for individual event pages
def event_detail(request, slug):
    queryset = Event.objects
    event = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "event/event_detail.html",
        {
            "event": event,
        }
    )


# View to handle the Create Event page
def create_event(request):
    event_form = CreateEventForm()
    time_hour = Event.TIME_CHOICES_12H
    time_ampm = Event.TIME_AMPM
    
    # I've tried strptime, I've splitting the inputs in 2 different ways, 1 as model CHOICES, 1 as creating 2 string
    # inputs in the form, getting them with request.POST.get() and combining them then formatting with strptime. 
    # Nothing has worked.
    # Constant error "this field is required" no matter the format of the input
    
    if request.method == "POST":
        event_form = CreateEventForm(request.POST)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.organizer = request.user

            event.save()
            messages.add_message(request, messages.SUCCESS, "You have created an event")
            return HttpResponseRedirect("success/")

        # Runs if form is invalid
        else:
            print("Form fail", event_form.errors)
            messages.add_message(request, messages.ERROR, "Your form was invalid")

    return render(request, "event/form_create_event.html", {"event_form":event_form, "time_hour":time_hour, "time_ampm":time_ampm})


# The page that the user is redirected to on valid form submission
def create_success(request):
    return render(request, "event/form_create_success.html")

def attend_event(request, slug):
    event = Event.objects.get(slug=slug)
    event.attendance_count = event.attendance_count + 1
    event.save()
    return HttpResponseRedirect(reverse('event_detail', args=[slug]))