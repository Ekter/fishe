from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Probe
from .models import Measure
from .serializers import ProbeSerializer
from .serializers import MeasureSerializer


class ProbeViewSet(viewsets.ModelViewSet):
    queryset = Probe.objects.all()
    serializer_class = ProbeSerializer


class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
