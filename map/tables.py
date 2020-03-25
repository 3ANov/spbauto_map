import django_tables2 as tables


from .models import ProblemLabel, ProblemLabelFilter
from django_tables2.utils import A
from django_filters.views import FilterView


class ProblemsTable(tables.Table):
    description = tables.TemplateColumn('{{value|truncatewords:9}}', orderable=False,)
    link = tables.LinkColumn("problem_details", text="подробно", args=[A("pk")], orderable=False, verbose_name="")

    class Meta:
        model = ProblemLabel
        fields = ("id", "description", "created_date")
        row_attrs = {
            "bgcolor": lambda record: record.status.color
        }





