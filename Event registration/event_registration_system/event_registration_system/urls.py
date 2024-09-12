from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from events import views as event_views  # Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_views.main_page, name='main_page'),
    path('create-event/', event_views.create_event, name='create_event'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('events/', event_views.event_list, name='event_list'),
    path('event/<int:event_id>/', event_views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', event_views.register_for_event, name='register_for_event'),
    path('my-registrations/', event_views.user_registrations, name='user_registrations'),
    path('event/<int:event_id>/cancel/', event_views.cancel_registration, name='cancel_registration'),

    path('', event_views.main_page, name='main_page'),
    path('create-event/', event_views.create_event, name='create_event'),
]
