# from django.db import models
from django.contrib.gis.db import models


class Salon(models.Model):
    place_id = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    types = models.TextField(null=True, blank=True)
    formatted_phone_number = models.CharField(max_length=50, null=True, blank=True)
    international_phone_number = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    emails = models.TextField(null=True, blank=True)
    formatted_address = models.CharField(max_length=50, null=True, blank=True)
    lng = models.FloatField(max_length=50, blank=True, null=True)
    lat = models.FloatField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    rating =  models.FloatField(null=True, blank=True)
    rated = models.IntegerField(null=True, blank=True)
    called = models.BooleanField(default=False)
    mailed = models.BooleanField(default=False)
    note = models.TextField(null=True, blank=True)
    crawled = models.BooleanField(default=False)

    def salon_link(self):
        url = "None"
        try:
            url = '<a href="%s">%s</a>' % (self.website, self.website)
        except:
            pass

        return url

    salon_link.allow_tags = True
    salon_link.short_description = "Website"