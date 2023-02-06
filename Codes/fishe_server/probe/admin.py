from django.contrib import admin

from probe import models

# Register your models here.

admin.site.register(models.Probe)
admin.site.register(models.Measure)
