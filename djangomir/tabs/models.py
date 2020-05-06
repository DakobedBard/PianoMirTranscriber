from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField
class Note():
    gString = models.CharField(blank=False, null=False)
    fret = models.CharField(blank=False, null=False),
    beat = models.IntegerField(blank=False, null=False)

class GuitarTab(models.Model):
    name = models.CharField(max_length=30, default="firstTab.txt")
    notes = ArrayField(JSONField(default=list), null=True)

