from django.contrib.gis.db import models


class CountyBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    statefp = models.CharField(max_length=10)
    countyfp = models.CharField(max_length=10)
    countyns = models.CharField(max_length=10)
    geoid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=10)
    classfp = models.CharField(max_length=10)

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name
