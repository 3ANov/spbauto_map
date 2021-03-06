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
    path('problems_set', views.problems_dataset, name='problems_data'),
    path('status_set', views.status_dataset, name='status_data'),
    #path("problems_list/", views.problems_list, name='problems_list'),
    path("problems_list/", views.ProblemsListView.as_view(), name='problems_list'),
    path("problem/<int:pk>/", views.problem_details, name="problem_details"),
    #path('data.geojson', GeoJSONLayerView.as_view(model=ProblemLabel), name='data'),

]
