from rest_framework import serializers
from ..models import Signalling


class SignallingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signalling
        fields = ['pk', 'type', 'address', 'latitude', 'longitude', 'coverage_area']