# coding = utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from news.models import *

def news_list(request):
    news = News.objects.filter(display=True)
    return render_to_response('news/news_list.html', {'news': news}, context_instance=RequestContext(request))

def news_show(request, id=''):
    try:
        news = News.objects.get(id=id, display=True)
    except News.DoesNotExist:
        raise Http404
    return render_to_response('news/news_show.html', {'news': news})