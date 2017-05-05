# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Details', fields ['name']
        db.create_unique(u'Events_details', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Details', fields ['name']
        db.delete_unique(u'Events_details', ['name'])


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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['Events']