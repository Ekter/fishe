from django.db import models


# Create your models here.

class Probe(models.Model):
    ip = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.name}>({self.ip})]"


class Measure(models.Model):
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE)
    temperature = models.FloatField()
    ph = models.FloatField(name="pH", verbose_name="pH")
    turbidity = models.FloatField()
    x_position = models.FloatField()
    y_position = models.FloatField()
    z_position = models.FloatField()

    def __str__(self):
        return f"<{self.probe.name}>" \
               f"({self.temperature}°C)" \
               f"({self.pH})" \
               f"({self.turbidity}NTU)" \
               f"({self.x_position}m)" \
               f"({self.y_position}m)" \
               f"({self.z_position}m)"
