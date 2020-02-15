from django.urls import path, re_path, include
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.auth import views as auth_views

from . import views

from .models import ProblemLabel

from django.contrib import admin



urlpatterns = [
    path('', views.home, name='home'),
    path('report', views.problem_report, name='report'),
    path('accounts/', include('accounts.urls')),
    re_path(r'^data.geojson$',
            GeoJSONLayerView.as_view(model=ProblemLabel,
                                     properties=('description', 'date_format')), name='data')

]
