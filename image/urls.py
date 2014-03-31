# coding = utf-8

from django.conf.urls import *

urlpatterns = patterns(('image.views'),
                       url(r'^$', 'image_show', name='image_show'),
                       url(r'^(?P<page>\d+)/$', 'image_show', name='image_show'),
                       )

