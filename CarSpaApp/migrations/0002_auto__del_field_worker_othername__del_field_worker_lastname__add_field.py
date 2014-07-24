# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Worker.othername'
        db.delete_column(u'CarSpaApp_worker', 'othername')

        # Deleting field 'Worker.lastname'
        db.delete_column(u'CarSpaApp_worker', 'lastname')

        # Adding field 'Worker.Full_Name'
        db.add_column(u'CarSpaApp_worker', 'Full_Name',
                      self.gf('django.db.models.fields.CharField')(default='Yaw', max_length=60),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Worker.othername'
        db.add_column(u'CarSpaApp_worker', 'othername',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 7, 15, 0, 0), max_length=30),
                      keep_default=False)

        # Adding field 'Worker.lastname'
        db.add_column(u'CarSpaApp_worker', 'lastname',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Deleting field 'Worker.Full_Name'
        db.delete_column(u'CarSpaApp_worker', 'Full_Name')


    models = {
        u'CarSpaApp.worker': {
            'Full_Name': ('django.db.models.fields.CharField', [], {'default': "'Yaw'", 'max_length': '60'}),
            'Meta': {'object_name': 'Worker'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date_Of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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