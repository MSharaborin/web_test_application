from django.urls import reverse

from django.db import models


class Signalling(models.Model):
    """
    Таблица с сигнализациями.
    """

    CHOICES = (
        ('siren', 'siren'),
        ('speaker', 'speaker'),
    )

    type = models.CharField(choices=CHOICES, max_length=25, verbose_name='Type_of_signalling',)
    address = models.CharField(max_length=255, verbose_name='Address with signalling',)
    latitude = models.FloatField(verbose_name='Latitude',)
    longitude = models.FloatField(verbose_name='Longitude',)
    coverage_area = models.IntegerField(verbose_name='Coverage area',)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('detail_url', args=[str(self.pk)])
