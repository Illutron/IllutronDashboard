from django.core import serializers

from django.utils import simplejson

from django.http import HttpResponse
from models import Entry
from django.contrib.auth.models import User

def latest(request):
    """
    Return a list of the latest entries for all members.
    """

    users = User.objects.all()
    data = []

    for user in users:
        entry = user.log_entries.all()[0]
        latest_checkin_entry = user.log_entries.filter(on_illutron=True)[0]

        if user.first_name and user.last_name:
            name = user.first_name + user.last_name
        else:
            name = user.username

        data.append({
            'member': name,
            'on_illutron': entry.on_illutron,
            'latest_checkin_time': latest_checkin_entry.time.isoformat(),
            #'last_log_entry': entry.time.isoformat(),
            #'latitude': entry.latitude,
            #'longitude': entry.longitude,

        })

    return HttpResponse(simplejson.dumps(data))
    