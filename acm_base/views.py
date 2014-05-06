# coding = utf-8

from django.shortcuts import render_to_response

import datetime
# from image.models import *
from news.models import *
from photologue.models import Photo


def index(request):
    image = Photo.objects.filter(index_show=True)[:5]
    news = News.objects.all()[:10]
    return render_to_response('index.html', {'image': image, 'news': news})