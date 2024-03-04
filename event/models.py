from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Event(models.Model):
    # Name of event
    title = models.CharField(max_length=150, unique=True)
    # URL for event post
    slug = models.SlugField(max_length=150, unique=True)
    # The associated user
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts"
    )
    # Main body of text
    content = models.TextField()
    # Time of creation
    created_on = models.DateTimeField(auto_now_add=True)
    # Time of update / edit of post
    updated_on = models.DateTimeField(auto_now=True)

    # Field for event hosting date
    event_date = models.DateTimeField()
    
    # Sets image field and default image
    image = CloudinaryField('image', default='placeholder')

