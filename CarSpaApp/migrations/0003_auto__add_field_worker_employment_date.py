# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Worker.datecreated'
        db.delete_column(u'CarSpaApp_worker', 'datecreated')

        # Deleting field 'Worker.dateupdated'
        db.delete_column(u'CarSpaApp_worker', 'dateupdated')

        # Adding field 'Worker.employment_date'
        db.add_column(u'CarSpaApp_worker', 'employment_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Worker.date_created'
        db.add_column(u'CarSpaApp_worker', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Worker.date_updated'
        db.add_column(u'CarSpaApp_worker', 'date_updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Worker.datecreated'
        db.add_column(u'CarSpaApp_worker', 'datecreated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Worker.dateupdated'
        db.add_column(u'CarSpaApp_worker', 'dateupdated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Worker.employment_date'
        db.delete_column(u'CarSpaApp_worker', 'employment_date')

        # Deleting field 'Worker.date_created'
        db.delete_column(u'CarSpaApp_worker', 'date_created')

        # Deleting field 'Worker.date_updated'
        db.delete_column(u'CarSpaApp_worker', 'date_updated')


    models = {
        u'CarSpaApp.worker': {
            'Full_Name': ('django.db.models.fields.CharField', [], {'default': "'Yaw'", 'max_length': '60'}),
            'Meta': {'object_name': 'Worker'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date_Of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'employment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'nextOfKin': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'place_Of_birth': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'residentialAddress': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'work_ID': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'work_detail': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['CarSpaApp']