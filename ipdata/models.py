import datetime

from django.db import models
from django.utils import timezone


class Ip(models.Model):
    ip = models.GenericIPAddressField()
    pais = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    pub_date = models.DateTimeField('data de pesquisa')
