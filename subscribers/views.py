from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import SubscriberForm


class SubscriberCreateView(CreateView):
    template_name = 'subscribe_form.html'
    form_class = SubscriberForm
    success_url = 'thanks/'

    def form_valid(self, form):
        loc_id = form.cleaned_data['user_location'].id
        form.instance.location_id = loc_id
        return super().form_valid(form)


class SubscriberCreateSuccessView(TemplateView):
    template_name = 'thanks.html'
