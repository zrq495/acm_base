# coding = utf-8

from django.conf.urls import *

urlpatterns = patterns(('news.views'),
                       url(r'^$', 'news_list', name='news_list'),
                       url(r'^(?P<id>\d+)/$', 'news_show', name='news_show'),
                       )