from dal import autocomplete
from .models import Location


class LocationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Location.objects.all()

        if self.q:
            qs = qs.filter(city__istartswith=self.q)

        return qs
