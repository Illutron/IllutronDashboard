from django.conf.urls.defaults import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'views.dashboard', name='dashboard'),

    url(r'^api/', include('log.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$',
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)