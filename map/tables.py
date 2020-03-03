import django_tables2 as tables
from .models import ProblemLabel


class ProblemsTable(tables.Table):
    description = tables.TemplateColumn(
        '{{value|truncatewords:9}}')
    class Meta:
        model = ProblemLabel
        fields = ("id", "description", "created_date")
        row_attrs = {
            "bgcolor": lambda record: record.status.color
        }

