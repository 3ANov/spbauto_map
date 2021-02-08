from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

# Create your views here.
from problem_register.filters import ProblemLabelFilter
from problem_register.forms import ProblemLabelForm
from problem_register.models import ProblemLabel, Status
from problem_register.tables import ProblemsTable


class ReportView(FormView):
    template_name = 'problem_register/report.html'
    form_class = ProblemLabelForm
    success_url = '/'


def problems_dataset(request):
    data = serialize('geojson', ProblemLabel.objects.all(), fields=('geom', 'description',
                                                                    'created_date', 'pk', 'status'))
    return HttpResponse(data, content_type="json")


def status_dataset(request):
    data = serialize('json', Status.objects.all())
    return HttpResponse(data, content_type="json")


class ProblemsListView(SingleTableMixin, FilterView):
    table_class = ProblemsTable
    model = ProblemLabel
    template_name = "problem_register/problems_list.html"
    filterset_class = ProblemLabelFilter


def problem_details(request, pk):
    return HttpResponseRedirect('/')