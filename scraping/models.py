from django.db import models
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название Города', unique=True)
    slug = models.CharField(max_length=25, unique=True, blank=True)

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Название Город'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(self.name)[:10]
        super().save(*args, **kwargs)



class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Языки программирования', unique=True)
    slug = models.CharField(max_length=25, unique=True, blank=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(self.name)[:10]
        super().save(*args, **kwargs)



