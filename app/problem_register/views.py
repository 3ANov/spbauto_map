from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin


from rest_framework import viewsets, generics

from problem_register.filters import ProblemLabelFilter
from problem_register.forms import ProblemLabelForm
from problem_register.models import ProblemLabel, ProblemStatus
from problem_register.serializers import StatusSerializer, ProblemLabelGeoSerializer, ProblemLabelDetailSerializer
from problem_register.tables import ProblemsTable


class ReportView(LoginRequiredMixin, CreateView):
    """ View для добавления новой дорожной проблемы """
    model = ProblemLabel
    template_name = 'problem_register/report.html'
    form_class = ProblemLabelForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status, _ = ProblemStatus.objects.get_or_create(name='Новая')
        return super(ReportView, self).form_valid(form)


class ProblemsListView(SingleTableMixin, FilterView):
    """ View для вывода списка проблем, с различными фильтрами """
    table_class = ProblemsTable
    model = ProblemLabel
    template_name = "problem_register/problems_list.html"
    filterset_class = ProblemLabelFilter


class ProblemDetailView(DetailView):
    """ View для вывода подробной информации о дорожной проблеме """
    model = ProblemLabel
    template_name = "problem_register/problem_details.html"


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    """ DRF_ViewSet для вывода списка статусов дорожных проблем """
    queryset = ProblemStatus.objects.all()
    serializer_class = StatusSerializer


class ProblemLabelGeoJsonViewSet(viewsets.ReadOnlyModelViewSet):
    """ DRF_ViewSet для вывода в формате GeoJson списка проблем """
    serializer_class = ProblemLabelGeoSerializer
    queryset = ProblemLabel.objects.all()


class ProblemLabelDetailAPIView(generics.RetrieveAPIView):
    """ DRF_View для вывода в детальной информации о дорожной проблеме """
    queryset = ProblemLabel.objects.all()
    serializer_class = ProblemLabelDetailSerializer
