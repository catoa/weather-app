from dal import autocomplete
from .models import Location
from django.db.models import Q


class LocationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Location.objects.all()

        if self.q:
            qs = qs.filter(Q(city__istartswith=self.q) | Q(state__istartswith=self.q))

        return qs
