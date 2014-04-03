#coding=utf-8

from django.conf.urls import *

urlpatterns = patterns(('contest.views'),
                       url(r'^$', 'contest', name='contest'),
                       url(r'^(?P<id>\w+)/$', 'contest', name='contest'),
                       # url(r'^provincial/$', 'provincial', name='provincial'),
                       # url(r'^regional/$', 'regional', name='regional'),
                       # url(r'^final/$', 'final', name='final'),
                       )