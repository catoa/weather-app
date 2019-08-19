from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    autocomplete_fields = ['location']


admin.site.register(Subscriber, SubscriberAdmin)
