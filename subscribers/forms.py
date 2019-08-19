from dal import autocomplete
from django import forms

from core.models import Location
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    user_location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=autocomplete.ModelSelect2(url='location-autocomplete')
    )

    class Meta:
        model = Subscriber
        fields = ('email', 'user_location',)
