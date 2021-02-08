from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

# Create your views here.

from .models import ProblemLabel, ProblemLabelForm, Status, ProblemLabelFilter
from site_settings.models import SiteSettings

from .tables import ProblemsTable


def home(request):
    sitesettings = SiteSettings.load()
    return render(request, 'problem_register/templates/problem_register/home.html', {'site_settings': sitesettings})


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
        return render(request, 'problem_register/templates/problem_register/report.html', {'site_settings': sitesettings,
                                                  'form': form})
    else:
        return HttpResponseRedirect('/')


def map_admin(request):
    sitesettings = SiteSettings.load()


def problems_dataset(request):
    #data = GeoJSONSerializer().serialize(ProblemLabel.objects.all(), use_natural_keys=True, with_modelname=False)
    data = serialize('geojson', ProblemLabel.objects.all(), fields=('geom', 'description',
                                                                    'created_date', 'pk', 'status'))
    return HttpResponse(data, content_type="json")


def status_dataset(request):
    data = serialize('json', Status.objects.all())
    return HttpResponse(data, content_type="json")


'''
def problems_list(request):
    site_settings = SiteSettings.load()
    problems_set = ProblemLabel.objects.all()
    table = ProblemsTable(problems_set)
    f = ProblemLabelFilter(request.GET, queryset=problems_set)
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    return render(request, 'problem_register/problems_list.html', {'table': table, 'site_settings': site_settings, 'filter': f})
'''


class ProblemsListView(SingleTableMixin, FilterView):
    sitesettings = SiteSettings.load()
    table_class = ProblemsTable
    model = ProblemLabel
    template_name = "problem_register/templates/problem_register/problems_list.html"
    filterset_class = ProblemLabelFilter
    extra_context = {'site_settings': sitesettings}


def problem_details(request, pk):
    return HttpResponseRedirect('/')
