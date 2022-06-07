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


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200, verbose_name='Заголовок вакансий')
    company = models.CharField(max_length=200, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание Вакансий')
    city = models.ForeignKey('City', verbose_name='', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', verbose_name='', on_delete=models.CASCADE)
    timestmp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
