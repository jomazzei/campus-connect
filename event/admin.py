from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Event)
# class TextEditAdmin(SummernoteModelAdmin):
    # !! This is where we'll add summernote fields after all the model fields are defined !!

admin.site.register(Event)