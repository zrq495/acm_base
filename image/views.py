#coding=utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from image.models import *


def image_show(request, page='1'):
    page_image = 24     # 每页图片的数量
    try:
        page = int(page)
        start = (page - 1) * page_image
        end = start + page_image
        count = Image.objects.all().count()
        #向上取整
        page_count = int((count + page_image - 1) / page_image)
        if page > page_count or page <= 0:
            raise
        image = Image.objects.all()[start:end]
    except (Image.DoesNotExist, TypeError):
        raise Http404
    return render_to_response('image/show.html', {'image': image, 'current_page':page, 'previous_page': page-1,
                                                  'next_page':page+1, 'page_count': page_count, 'page_list': [i+1 for i in range(page_count)]})