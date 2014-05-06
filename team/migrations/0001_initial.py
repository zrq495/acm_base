# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TeamList'
        db.create_table('team_teamlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('team_identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('team_introduction', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('team', ['TeamList'])

        # Adding model 'Team'
        db.create_table('team_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team_identifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.TeamList'], to_field='team_identifier')),
            ('team_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('team_member', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('team', ['Team'])


    def backwards(self, orm):
        # Deleting model 'TeamList'
        db.delete_table('team_teamlist')

        # Deleting model 'Team'
        db.delete_table('team_team')


    models = {
        'team.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_identifier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team.TeamList']", 'to_field': "'team_identifier'"}),
            'team_member': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'team.teamlist': {
            'Meta': {'object_name': 'TeamList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'team_introduction': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['team']