import time

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
    geom = gismodels.GeometryField()

    @property
    def status_name(self):
        self.status.name



    #return self.created_date.strftime('%d-%m-%Y %H:%M')
    @property
    def date_format(self):
        return self.created_date.strftime('%d-%m-%Y %H:%M')

    def save(self, *args, **kwargs):
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
