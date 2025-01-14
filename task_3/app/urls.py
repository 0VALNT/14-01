from django.urls import path
from .views import EventCreate, EventList, EventDetail, AttendeeCreate, AttendeeList, AttendeeDetail

urlpatterns = [
    path('event/create', EventCreate.as_view(), name='event_create'),
    path('event/detail/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('event/list', EventList.as_view(), name='event_list'),

    path('attendee/create', AttendeeCreate.as_view(), name='attendee_create'),
    path('attendee/detail/<int:pk>', AttendeeDetail.as_view(), name='attendee_detail'),
    path('attendee/list', AttendeeList.as_view(), name='attendee_list'),
]
from .views import AttendeeUpdate, EventUpdate, delete_event, delete_attendee

urlpatterns += [
    path('event/delete/<int:pk>', delete_event, name='event_delete'),
    path('attendee/delete/<int:pk>', delete_attendee, name='attendee_delete'),
    path('attendee/update/<int:pk>', AttendeeUpdate.as_view(), name='attendee_update'),
    path('event/update/<int:pk>', EventUpdate.as_view(), name='event_update'),
]
