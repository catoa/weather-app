from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    state_abbrev = models.CharField(max_length=2)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ["city"]

    def __str__(self):
        return f"{self.city}, {self.state_abbrev}"
