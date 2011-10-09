from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User

def latest(request):
    """
    Return a list of the latest entries for all members.
    """

    users = User.objects.all()
    data = []

    for user in users:
        try:
            entry = user.log_entries.all()[0]

            try:
                latest_checkin_entry = user.log_entries.filter(on_illutron=True)[0].time.isoformat()
            except:
                latest_checkin_entry = False

            if user.first_name and user.last_name:
                name = user.first_name + " " + user.last_name
            else:
                name = user.username

            try:
                image = user.get_profile().image.url
            except:
                image = False

            data.append({
                'member': name,
                'on_illutron': entry.on_illutron,
                'latest_checkin_time': latest_checkin_entry,
                'image': image
                #'last_log_entry': entry.time.isoformat(),
                #'latitude': entry.latitude,
                #'longitude': entry.longitude,
            })

        except:
            pass


    return HttpResponse(simplejson.dumps(data), mimetype='application/json')
