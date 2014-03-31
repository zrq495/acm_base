# coding = utf-8

from django.shortcuts import render_to_response

import datetime

from image.models import *

def index(request):
    image = Image.objects.all()[:5]
    return render_to_response('index.html', {'image': image})