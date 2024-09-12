from django.urls import path
from .views import event_list, event_detail, register_for_event, user_registrations, cancel_registration, main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('events/', event_list, name='event_list'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', register_for_event, name='register_for_event'),
    path('my-registrations/', user_registrations, name='user_registrations'),
    path('event/<int:event_id>/cancel/', cancel_registration, name='cancel_registration'),
]
