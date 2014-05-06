#coding=utf-8

from django.db import models


class TeamList(models.Model):
    team_name = models.CharField(max_length=100)
    team_identifier = models.CharField(max_length=100, unique=True, )
    # team_introduction = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.team_identifier, )


class Team(models.Model):
    team_identifier = models.ForeignKey(TeamList, 'team_identifier')
    team_year = models.PositiveSmallIntegerField()
    team_member = models.TextField(blank=True)