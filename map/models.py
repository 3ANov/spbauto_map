import django_filters
import requests
from colorfield.fields import ColorField
from django.conf import settings
from django.db import models
from django.contrib.gis.db import models as gismodels
from django import forms
from django.utils import timezone
from leaflet.forms.widgets import LeafletWidget


# Create your models here.


class Road(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StateDistrict(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)
    color = ColorField()

    def __str__(self):
        return self.name


class ProblemLabel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="№")
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

    def save(self, *args, **kwargs):
        response = requests.get('http://localhost:8080/reverse?lon=' + str(self.geom.x) + '&lat=' + str(self.geom.y))
        json_response = response.json()
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


class ProblemLabelFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())

    state_district = django_filters.CharFilter(field_name='state_district__name',
                                               lookup_expr='icontains',
                                               label='Район насёленного пункта')

    place = django_filters.CharFilter(field_name='place__name',
                                      lookup_expr='icontains',
                                      label='Населённый пункт')

    county = django_filters.CharFilter(field_name='county__name',
                                       lookup_expr='icontains',
                                       label='Район области')

    road = django_filters.CharFilter(field_name='road__name',
                                     lookup_expr='icontains',
                                     label='Улица')

    id = django_filters.NumberFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = ProblemLabel
        fields = ['id', 'status', 'county', 'place', 'state_district', 'road']
