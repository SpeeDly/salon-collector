# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Salon'
        db.create_table('beauty_salon_salon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('types', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('formatted_phone_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('international_phone_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True, null=True)),
            ('emails', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('formatted_address', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(max_length=50, blank=True, null=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(max_length=50, blank=True, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(blank=True, null=True)),
            ('rated', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('called', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mailed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('beauty_salon', ['Salon'])


    def backwards(self, orm):
        # Deleting model 'Salon'
        db.delete_table('beauty_salon_salon')


    models = {
        'beauty_salon.salon': {
            'Meta': {'object_name': 'Salon'},
            'called': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
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