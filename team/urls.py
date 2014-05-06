from django.conf.urls import *

urlpatterns = patterns(('team.views'),
                       url(r'^$', 'team', name='team'),
                       url(r'^(?P<id>\w+)/$', 'team', name='team')
                       )