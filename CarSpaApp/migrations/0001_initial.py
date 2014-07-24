# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Worker'
        db.create_table(u'CarSpaApp_worker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_ID', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('othername', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('work_detail', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50, unique=True, null=True, blank=True)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('residentialAddress', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('date_Of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('place_Of_birth', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('blood_group', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('nextOfKin', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('datecreated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('dateupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'CarSpaApp', ['Worker'])


    def backwards(self, orm):
        # Deleting model 'Worker'
        db.delete_table(u'CarSpaApp_worker')


    models = {
        u'CarSpaApp.worker': {
            'Meta': {'object_name': 'Worker'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date_Of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'nextOfKin': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'othername': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'place_Of_birth': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'residentialAddress': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'work_ID': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'work_detail': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['CarSpaApp']