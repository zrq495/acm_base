# coding = utf-8

from django.conf.urls import patterns, include, url

from acm_base.views import *

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acm_base.views.home', name='home'),
    # url(r'^acm_base/', include('acm_base.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
)

urlpatterns += patterns((''),
                        (r'^photo/', include('photologue.urls')),
                        (r'^news/', include('news.urls')),
                        (r'^show/', include('image.urls')),
                        (r'^contest/', include('contest.urls')),
                        (r'^team/', include('team.urls')),
                        )

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r"^media/(?P<path>.*)$", 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                            )