from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from problem_register.models import ProblemStatus, ProblemLabel


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemStatus
        fields = '__all__'


class ProblemLabelGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ProblemLabel
        geo_field = 'geom'
        fields = ['id', 'status']


class ProblemLabelDetailSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField(many=False)
    place = serializers.StringRelatedField(many=False)
    state_district = serializers.StringRelatedField(many=False)
    county = serializers.StringRelatedField(many=False)
    road = serializers.StringRelatedField(many=False)

    class Meta:
        model = ProblemLabel
        exclude = ['author', 'geom']

