# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TeamList.team_introduction'
        db.delete_column('team_teamlist', 'team_introduction')


    def backwards(self, orm):
        # Adding field 'TeamList.team_introduction'
        db.add_column('team_teamlist', 'team_introduction',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


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
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['team']