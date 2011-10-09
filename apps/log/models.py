from django.db import models
from django.contrib.auth.models import User
import datetime

class Provider(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    member = models.ForeignKey(User, related_name='log_entries')
    description = models.TextField(blank=True)
    time = models.DateTimeField(default=datetime.datetime.now)
    on_illutron = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, help_text="accuracy in meters.", null=True)
    provider = models.ForeignKey(Provider)

    def __unicode__(self):
        s = ""
        if not self.on_illutron:
            s = " not"
        return "%s is%s on Illutron" % (self.member.username, s)
    
