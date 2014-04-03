#coding=utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from contest.models import *


def contest(request, id='introduction'):
    try:
        con = Contest.objects.get(identifier=id)
        con_list = Contest.objects.select_related('contest_name', 'identifier')
    except Contest.DoesNotExist:
        raise Http404
    return render_to_response('contest/contest.html', {'contest': con, 'contest_list': con_list})