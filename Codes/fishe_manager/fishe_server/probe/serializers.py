from rest_framework import serializers
from .models import Probe
from .models import Measure


class ProbeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Probe
        fields = '__all__'


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = '__all__'
