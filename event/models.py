from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    TIME_CHOICES_12H = [
    (1, "1:00"),
    (2, "2:00"),
    (3, "3:00"),
    (4, "4:00"),
    (5, "5:00"),
    (6, "6:00"),
    (7, "7:00"),
    (8, "8:00"),
    (9, "9:00"),
    (10, "10:00"),
    (11, "11:00"),
    (12, "12:00")
    ]

    TIME_AMPM = [
    ("AM", "AM"),
    ("PM", "PM")
    ]

    # Name of the event
    title = models.CharField(max_length=200, unique=True)
    # URL field
    slug = models.SlugField(max_length=250, unique=True)
    # The date the event is held
    event_host_date = models.DateTimeField()
    # Time of event
    event_host_time = models.IntegerField(choices=TIME_CHOICES_12H, default=1)
    event_host_time_AMPM = models.CharField(max_length=2, choices=TIME_AMPM, default="AM")
    # Where the event is held
    venue = models.CharField(max_length=200)
    # Organizer is the user account that created event post
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="event_posts")
    # Cloudinary image field
    featured_image = CloudinaryField('image', default='placeholder')
    # Main content
    content = models.TextField(null=False)
    # Max people event can hold
    max_people = models.IntegerField(null=True)
    # Attendance tracker for users
    attendance_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["event_host_date", "organizer"]

    # Returns title of post in admin panel instead of "Object(n)"
    def __str__(self):
        return f"{self.title} | posted by {self.organizer}"