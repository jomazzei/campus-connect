from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .forms import CreateEventForm


# Checks if is.valid() = True.
# assertTrue checks if (argument) is true
class TestEventForm(TestCase):

    def test_form_is_valid(self):

        event_form = CreateEventForm({
            "title": "This is the name of Event",
            "venue": "Bristol",
            "event_host_date": "04/12/2024",
            "event_host_time": '10:00:00',
            "content": "This is the body of the post",
            "max_people": 20,
        })
        if not event_form.is_valid():
            for field, errors in event_form.errors.items():
                print(f"Field: {field}")
                for error in errors:
                    print(f"Error: {error}")

        self.assertTrue(event_form.is_valid(), msg='Form is not valid')