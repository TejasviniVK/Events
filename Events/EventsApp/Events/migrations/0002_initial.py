# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Details'
        db.create_table(u'Events_details', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'Events', ['Details'])

        # Adding model 'Cities'
        db.create_table(u'Events_cities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'Events', ['Cities'])


    def backwards(self, orm):
        # Deleting model 'Details'
        db.delete_table(u'Events_details')

        # Deleting model 'Cities'
        db.delete_table(u'Events_cities')


    models = {
        u'Events.cities': {
            'Meta': {'object_name': 'Cities'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Events.details': {
            'Meta': {'object_name': 'Details'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Events']