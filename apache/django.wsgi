import os
import sys
import site

site.addsitedir('/home/illutron/.virtualenvs/IllutronDashboard/lib/python2.7/site-packages')

sys.path.append('/home/illutron/srv/')
sys.path.append('/home/illutron/srv/IllutronDashboard/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'IllutronDashboard.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
