from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('log.views',

    url(r'^latest/$',
        'latest',
        name='api_latest'
    ),

)
