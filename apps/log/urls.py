from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('log.views',

    url(r'^members/(?P<id>\d+)/$',
        'member',
        name='api_member'
    ),

    url(r'^members/$',
        'member_list',
        name='api_member_list'
    ),


    
)
