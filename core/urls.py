from .views import LocationAutocomplete
from django.urls import path

urlpatterns = [
    path(
        'location/',
        LocationAutocomplete.as_view(),
        name='location-autocomplete',
    ),
]