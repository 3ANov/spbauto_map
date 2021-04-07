from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

# Create your views here.
from main.celery import debug_task
from problem_register.filters import ProblemLabelFilter
from problem_register.forms import ProblemLabelForm
from problem_register.models import ProblemLabel, Status
from problem_register.tables import ProblemsTable
from problem_register.tasks import add_places_task


class ReportView(LoginRequiredMixin, CreateView):
    """ View для добавления новой дорожной проблемы """
    model = ProblemLabel
    template_name = 'problem_register/report.html'
    form_class = ProblemLabelForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status, _ = Status.objects.get_or_create(name='Новая')
        return super(ReportView, self).form_valid(form)


def problems_dataset(request):
    data = serialize('geojson', ProblemLabel.objects.all(), fields=('geom', 'description',
                                                                    'created_date', 'pk', 'status'))
    return HttpResponse(data, content_type="json")


def status_dataset(request):
    data = serialize('json', Status.objects.all())
    return HttpResponse(data, content_type="json")


class ProblemsListView(SingleTableMixin, FilterView):
    """ View для вывода списка проблем, с различными фильтрами"""
    table_class = ProblemsTable
    model = ProblemLabel
    template_name = "problem_register/problems_list.html"
    filterset_class = ProblemLabelFilter


class ProblemDetailView(DetailView):
    model = ProblemLabel
    template_name = "problem_register/problem_details.html"

