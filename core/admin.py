from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    search_fields = ['city', ]


admin.site.register(Location, LocationAdmin)
