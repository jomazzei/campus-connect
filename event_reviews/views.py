from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, EventReview
from .models import Event

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    reviews = EventReview.objects.filter(event=event)
    return render(request, 'event_reviews/event_detail.html', {'event': event, 'reviews': reviews})

@login_required
def add_event_review(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(pk=event_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        EventReview.objects.create(user=request.user, event=event, rating=rating, comment=comment)
        return redirect('event_detail', event_id=event_id)
    else:
        return render(request, 'event_reviews/add_event_review.html', {'event_id': event_id})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_reviews/event_list.html', {'events': events})
