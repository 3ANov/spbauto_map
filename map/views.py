from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from djgeojson.views import GeoJSONLayerView

from .models import ProblemLabel, ProblemLabelForm, Status
from sitesettings.models import SiteSettings
from djgeojson.serializers import Serializer as GeoJSONSerializer




def home(request):
    sitesettings = SiteSettings.load()
    return render(request, 'map/home.html', {'sitesettings': sitesettings})


def problem_report(request):
    sitesettings = SiteSettings.load()
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProblemLabelForm(request.POST)
            if form.is_valid():
                report = form.save(commit=False)
                report.author = request.user
                report.save()
                return HttpResponseRedirect('/')
        else:
            form = ProblemLabelForm()
        return render(request, 'map/report.html', {'sitesettings': sitesettings,
                                                  'form': form})
    else:
        return HttpResponseRedirect('/')


def map_admin(request):
    sitesettings = SiteSettings.load()


def problems_dataset(request):
    #data = GeoJSONSerializer().serialize(ProblemLabel.objects.all(), use_natural_keys=True, with_modelname=False)
    data = serialize('geojson', ProblemLabel.objects.all(), fields=('geom', 'author'))
    return HttpResponse(data, content_type="json")
