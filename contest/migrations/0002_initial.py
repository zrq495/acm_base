# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContestList'
        db.create_table('contest_contestlist', (
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
        ))
        db.send_create_signal('contest', ['ContestList'])

        # Adding model 'Contest'
        db.create_table('contest_contest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contest_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('identifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contest.ContestList'])),
            ('introduction', self.gf('django.db.models.fields.TextField')()),
            ('award', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('contest', ['Contest'])


    def backwards(self, orm):
        # Deleting model 'ContestList'
        db.delete_table('contest_contestlist')

        # Deleting model 'Contest'
        db.delete_table('contest_contest')


    models = {
        'contest.contest': {
            'Meta': {'object_name': 'Contest'},
            'award': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contest_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contest.ContestList']"}),
            'introduction': ('django.db.models.fields.TextField', [], {})
        },
        'contest.contestlist': {
            'Meta': {'object_name': 'ContestList'},
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        }
    }

    complete_apps = ['contest']