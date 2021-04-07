import django_filters

from problem_register.models import Status, ProblemLabel


class ProblemLabelFilter(django_filters.FilterSet):
    """ Фильтр для модели дорожной проблемы """
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
    '''                              
    road = django_filters.ModelChoiceFilter(queryset=Road.objects.all(),
                                     label='Улица')
    '''

    id = django_filters.NumberFilter(field_name='id', min_value=1, label='Номер проблемы')

    class Meta:
        model = ProblemLabel
        fields = ['id', 'status', 'county', 'place', 'state_district', 'road']
