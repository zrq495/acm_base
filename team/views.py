#coding=utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from team.models import *


def team(request):
    pass