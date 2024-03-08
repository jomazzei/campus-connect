from django.urls import path,include
from .views import event_detail, add_event_review
from .views import event_list

urlpatterns = [
    path('', event_list, name='event_list'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('<int:event_id>/', add_event_review, name='add_event_review'),

]




