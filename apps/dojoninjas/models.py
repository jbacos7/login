# Create your models here.
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255)

class Ninjas(models.Model):
    dojos = models.ForeignKey(Dojos, related_name = "ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
