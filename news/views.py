#coding=utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from news.models import *


def news_list(request, page_id='1'):
    page_news = 2      # 每页新闻数量
    try:
        page_id = int(page_id)
        start = (page_id-1) * page_news
        end = start + page_news
        count = News.objects.filter(display=True).count()
        # 向上取整
        page_count = int((count + page_news -1) / page_news)
        if page_id > page_count or page_id <= 0:
            raise
        news = News.objects.filter(display=True)[start:end]
    except (News.DoesNotExist, TypeError):
        raise Http404
    return render_to_response('news/news_list.html', {'news': news, 'current_page': page_id, 'previous_page': page_id-1,
                                                      'next_page': page_id+1, 'page_count': page_count,
                                                      'page_list': [i+1 for i in range(page_count)]})


def news_show(request, id=''):
    try:
        news = News.objects.get(id=id, display=True)
    except News.DoesNotExist:
        raise Http404
    return render_to_response('news/news_show.html', {'news': news})