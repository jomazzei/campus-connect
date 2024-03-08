from . import views
from django.urls import path

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.AboutPage, name="about-page"),
    path("allevents/", views.EventList.as_view(), name="event-list"),
    
    path("create/", views.create_event, name="create-new-form"),
    path("create/success/", views.create_success, name="create-new-success"),

    path("<slug:slug>/", views.event_detail, name="event_detail"),
    path("<slug:slug>/attend", views.attend_event, name="attend_event"),
    path("<slug:slug>/delete", views.delete_event, name="delete_event"),
]