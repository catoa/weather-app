from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from core.models import Location


class Subscriber(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self):
        return self.email
