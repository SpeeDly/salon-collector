# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Salon.crawled'
        db.add_column('beauty_salon_salon', 'crawled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Salon.crawled'
        db.delete_column('beauty_salon_salon', 'crawled')


    models = {
        'beauty_salon.salon': {
            'Meta': {'object_name': 'Salon'},
            'called': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'crawled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'emails': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'formatted_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'international_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'mailed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'place_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'rated': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'types': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['beauty_salon']