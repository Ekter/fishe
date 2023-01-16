# tests/factories.py
from factory import Faker
import factory

from ..models import Probe
from ..models import Measure


class ProbeFactory(factory.django.DjangoModelFactory):
    ip = Faker('ipv4')
    name = Faker('fishe_1')
    str = f"<{self.name}>({self.ip})"
    fake_str = ""

    class Meta:
        model = Probe


class MeasureFactory(factory.django.DjangoModelFactory):
    probe = factory.SubFactory(ProbeFactory)
    temperature = Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    ph = Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    turbidity = Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    x_position = Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    y_position = Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    z_position = Faker('pyfloat', left_digits=2, right_digits=2, positive=True)


    class Meta:
        model = Measure
