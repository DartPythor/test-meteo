from django.db import models


class CityCached(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        help_text="Название города",
        max_length=124,
    )
    latitude = models.FloatField(
        null=False,
        blank=False,
        help_text="Широта города",
    )
    longitude = models.FloatField(
        null=False,
        blank=False,
        help_text="Долгота города",
    )
    country = models.CharField(
        null=False,
        blank=False,
        help_text="Страна города",
        max_length=124,
    )

    def __str__(self):
        return f"CityCached[{self.name}] {self.country} - ({self.latitude}, {self.longitude})"
