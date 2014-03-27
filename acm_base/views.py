# coding = utf-8

from django.shortcuts import render_to_response

import datetime

def index(request):
    now = datetime.datetime.now()
    a = [i for i in range(100)]
    return render_to_response('index.html', {'now': now, 'a': a})