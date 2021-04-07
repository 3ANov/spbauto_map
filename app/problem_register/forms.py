from django import forms
from leaflet.forms.widgets import LeafletWidget

from problem_register.models import ProblemLabel


class ProblemLabelForm(forms.ModelForm):
    """ Форма для добавления новой дорожной проблемы """
    class Meta:
        model = ProblemLabel
        fields = ('description', 'geom')
        labels = {
            'description': '',
            'geom': '',
        }
        widgets = {'description': forms.Textarea(attrs={"rows": 5, "cols": 10, 'placeholder': 'Описание проблемы'}),
                   'geom': LeafletWidget()}
