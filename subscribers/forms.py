from dal import autocomplete
from django import forms

from core.models import Location
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.fields['user_location'].label = "Location"

    user_location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=autocomplete.ModelSelect2(url='location-autocomplete')
    )

    class Meta:
        model = Subscriber
        fields = ('email', 'user_location',)
