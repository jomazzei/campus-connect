from . import views
from django.urls import path

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path("create/", views.create_event, name="create-new-form"),
    path("create/success/", views.create_success, name="create-new-success"),
    path("about/", views.AboutPage, name="about-page"),
]