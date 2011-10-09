from pprint import pprint
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User


def member(request, id):

    user = get_object_or_404(User, id=id)

    log_entries = user.log_entries.all()[:10]
    try:
        log_entries[0]
    except:
        return HttpResponse("No activity yet")

    if user.first_name and user.last_name:
        name = user.first_name + " " + user.last_name
    else:
        name = user.username

    try:
        latest_checkin_entry = user.log_entries.filter(on_illutron=True)[0].time.isoformat()
    except IndexError:
        latest_checkin_entry = None

    try:
        image = user.get_profile().image.url
    except:
        image = None

    log_list = []
    for log in log_entries:
       log_list.append({
           'latitude': log.latitude,
           'longitude': log.longitude,
           'on_illutron': log.on_illutron,
           'time': log.time.isoformat(),
           'description': log.description
       })

    data = {
        'name': name,
        'on_illutron': log_entries[0].on_illutron,
        'latest_checkin_time': latest_checkin_entry,
        'image': image,
        'log': log_list
    }

    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def member_list(request):
    """
    Return a list of all members.
    """

    data = simplejson.dumps(list(User.objects.all().values('id', 'username',)))
    return HttpResponse(data, mimetype='application/json')
