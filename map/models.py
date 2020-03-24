import time
import urllib
import json

import pytz
from colorfield.fields import ColorField
from django.conf import settings
from django.db import models

from django.contrib.gis.db import models as gismodels
# Create your models here.
from django.forms import ModelForm
from django import forms
from django.contrib.gis import forms as gisforms
from django.utils import timezone
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget


class Road(models.Model):
    name = models.CharField(max_length=100)


class Place(models.Model):
    name = models.CharField(max_length=100)


class County(models.Model):
    name = models.CharField(max_length=100)


class StateDistrict(models.Model):
    name = models.CharField(max_length=100)


class Status(models.Model):
    name = models.CharField(max_length=20)
    color = ColorField()


class ProblemLabel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="№")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               verbose_name="добавлено пользователем")
    description = models.CharField(max_length=500, verbose_name="описание проблемы")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="время добавления")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="статус проблемы")
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="район области")
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="населённый пункт")
    state_district = models.ForeignKey(StateDistrict, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="район города")
    road = models.ForeignKey(Road, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="дорога")
    house_number = models.CharField(max_length=50, verbose_name="номер дома", blank=True)
    geom = gismodels.PointField()

    @property
    def status_name(self):
        self.status.name



    #return self.created_date.strftime('%d-%m-%Y %H:%M')
    @property
    def date_format(self):
        return self.created_date.strftime('%d-%m-%Y %H:%M')

    def save(self, *args, **kwargs):
        response = urllib.request.urlopen('http://localhost:8080/reverse?lon=' + str(self.geom.x)
                                          + '&lat=' + str(self.geom.y)).read()
        json_response = json.loads(response.decode('utf-8'))

        if 'county' in json_response['address']:
            print(json_response['address']['county'])
            self.county, created = County.objects.get_or_create(name=json_response['address']['county'])

        place_keys = ['city', 'town', 'village']
        for key in place_keys:
            if key in json_response['address']:
                print(json_response['address'][key])
                self.place, created = Place.objects.get_or_create(name=json_response['address'][key])

        if 'road' in json_response['address']:
            print(json_response['address']['road'])
            self.road, created = Road.objects.get_or_create(name=json_response['address']['road'])

        if 'state_district' in json_response['address']:
            print(json_response['address']['state_district'])
            self.state_district, created = \
                StateDistrict.objects.get_or_create(name=json_response['address']['state_district'])

        if 'house_number' in json_response['address']:
            print(json_response['address']['house_number'])
            self.house_number = json_response['address']['house_number']

        if self.status is None:
            self.status, created = Status.objects.get_or_create(id=1)
        super(ProblemLabel, self).save(*args, **kwargs)


class ProblemLabelForm(forms.ModelForm):
    class Meta:
        model = ProblemLabel
        fields = ('description', 'geom')
        labels = {
            'description': '',
            'geom': '',
        }
        widgets = {'description': forms.Textarea(attrs={"rows": 5, "cols": 10, 'placeholder': 'Описание проблемы'}),
                   'geom': LeafletWidget()}
