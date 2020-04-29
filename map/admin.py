from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import ProblemLabel, Status

# Register your models here.


#admin.site.register(ProblemLabel, LeafletGeoAdmin)
admin.site.register(Status)


@admin.register(ProblemLabel)
class ProblemLabelAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_display = ('id', 'description', 'created_date', 'road', 'house_number', 'place', 'status')