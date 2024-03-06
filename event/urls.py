from . import views
from django.urls import path

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path("create/", views.CreateForm, name="create-new-form"),
    path("about/", views.AboutPage, name="about-page"),
]