from django.conf.urls import *

urlpatterns = patterns(('team.views'),
                       url(r'^$', 'team', name='team'),
                       )