#coding=utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from team.models import *


def team(request, id='introducation'):
    tall = TeamList.objects.all()
    tl = TeamList.objects.get(team_identifier=id)
    t = tl.team_set.all().order_by('-team_year')
    return render_to_response('team/team.html', {'team': t, 'tall': tall})