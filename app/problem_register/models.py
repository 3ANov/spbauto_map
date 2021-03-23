from colorfield.fields import ColorField
from django.conf import settings
from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils import timezone
from places.models import County, Place, StateDistrict, Road


class Status(models.Model):
    """ Модель для хранения статуса проблемы"""
    """ ex: 'Новая', 'Решённая' и т.д. """

    name = models.CharField(max_length=20)
    color = ColorField()

    def __str__(self):
        return self.name


class ProblemLabel(models.Model):
    """ Модель для хранения данных о дорожной проблеме"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               verbose_name="добавлено пользователем")
    description = models.CharField(max_length=500, verbose_name="описание проблемы")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="время добавления")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="статус проблемы")
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="район области")
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="населённый пункт")
    state_district = models.ForeignKey(StateDistrict, on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name="район города")
    road = models.ForeignKey(Road, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="дорога")
    house_number = models.CharField(max_length=50, verbose_name="номер дома", blank=True)
    geom = gismodels.PointField()
