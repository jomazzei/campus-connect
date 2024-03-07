from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Event(models.Model):

    # Name of the event
    title = models.CharField(max_length=200, unique=True, blank=False)
    # URL field
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    # The date the event is held
    event_host_date = models.DateField()
    # Time of event
    event_host_time = models.TimeField()
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
    # Who is attending
    attendance_list = models.TextField(blank=True)

    class Meta:
        ordering = ["event_host_date", "organizer"]

    # Returns title of post in admin panel instead of "Object(n)"
    def __str__(self):
        return f"{self.title} | posted by {self.organizer}"

    def save(self, *args, **kwargs):
        """
        Generates a unique slug based on the post title
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)