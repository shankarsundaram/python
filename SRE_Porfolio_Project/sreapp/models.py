from django.db import models

# Create your models here.

class Sre(models.Model):
    client_name = models.CharField(max_legth=100)
    description = models.CharField(max_length=255)
    uptime = models.TimeField()
    downtime = models.TimeField()
    availability = models.FloatField()
    mttr = models.FloatField()
    mtbf = models.FloatField()
    sla = models.FloatField()
    slo = models.FloatField()
    sli = models. FloatField()
    error_budget = models.FloatField()