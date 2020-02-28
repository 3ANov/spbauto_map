from django_tables2 import tables
from .models import ProblemLabel


class ProblemsTable(tables.Table):
    class Meta:
        model = ProblemLabel
        template_name = "django_tables2/bootstrap4.html"
        fields = ("pk", "description", "geom")
        row_attrs = {
            "bgcolor": lambda record: record.status.color
        }
