from pprint import pprint
from django.core import serializers
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User


def member(request, id):

    user = User.objects.get(id=id)

    try:
        log_entries = user.log_entries.all()[:10]
    except:
        return HttpResponse("No activity yet.")

    if user.first_name and user.last_name:
        name = user.first_name + " " + user.last_name
    else:
        name = user.username

    try:
        latest_checkin_entry = user.log_entries.filter(on_illutron=True)[0].time.isoformat()
    except:
        latest_checkin_entry = None

    try:
        image = user.get_profile().image.url
    except:
        image = False

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

    data = simplejson.dumps(list(User.objects.all().values('id', 'username', 'first_name', 'last_name')))
    return HttpResponse(data, mimetype='application/json')
