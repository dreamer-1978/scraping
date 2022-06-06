from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название Города')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Название Город'

    def __str__(self):
        return self.name
