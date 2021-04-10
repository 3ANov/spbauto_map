from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from problem_register.models import Status, ProblemLabel


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name', 'color']


class ProblemLabelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ProblemLabel
        geo_field = 'geom'
        fields = []
