# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Wash_Type'
        db.create_table(u'CarSpaApp_wash_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'CarSpaApp', ['Wash_Type'])

        # Adding model 'Service_Rendered'
        db.create_table(u'CarSpaApp_service_rendered', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serviceID', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('service_Name', self.gf('django.db.models.fields.related.ForeignKey')(max_length=30, to=orm['CarSpaApp.Wash_Type'], null=True, blank=True)),
            ('car_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CarSpaApp.Car_Type'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CarSpaApp.Service_Category'])),
            ('price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'CarSpaApp', ['Service_Rendered'])

        # Adding model 'Car_Type'
        db.create_table(u'CarSpaApp_car_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'CarSpaApp', ['Car_Type'])

        # Adding model 'Service_Category'
        db.create_table(u'CarSpaApp_service_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'CarSpaApp', ['Service_Category'])


    def backwards(self, orm):
        # Deleting model 'Wash_Type'
        db.delete_table(u'CarSpaApp_wash_type')

        # Deleting model 'Service_Rendered'
        db.delete_table(u'CarSpaApp_service_rendered')

        # Deleting model 'Car_Type'
        db.delete_table(u'CarSpaApp_car_type')

        # Deleting model 'Service_Category'
        db.delete_table(u'CarSpaApp_service_category')


    models = {
        u'CarSpaApp.car_type': {
            'Meta': {'object_name': 'Car_Type'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'CarSpaApp.service_category': {
            'Meta': {'object_name': 'Service_Category'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'CarSpaApp.service_rendered': {
            'Meta': {'object_name': 'Service_Rendered'},
            'car_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CarSpaApp.Car_Type']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CarSpaApp.Service_Category']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'serviceID': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'service_Name': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '30', 'to': u"orm['CarSpaApp.Wash_Type']", 'null': 'True', 'blank': 'True'})
        },
        u'CarSpaApp.wash_type': {
            'Meta': {'object_name': 'Wash_Type'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
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