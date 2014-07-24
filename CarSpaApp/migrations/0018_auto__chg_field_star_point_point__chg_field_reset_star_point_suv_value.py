# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Star_Point.point'
        db.alter_column(u'CarSpaApp_star_point', 'point', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Reset_Star_Point.suv_value'
        db.alter_column(u'CarSpaApp_reset_star_point', 'suv_value', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Reset_Star_Point.value'
        db.alter_column(u'CarSpaApp_reset_star_point', 'value', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Reset_Star_Point.saloon_value'
        db.alter_column(u'CarSpaApp_reset_star_point', 'saloon_value', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'Star_Point.point'
        db.alter_column(u'CarSpaApp_star_point', 'point', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Reset_Star_Point.suv_value'
        db.alter_column(u'CarSpaApp_reset_star_point', 'suv_value', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Reset_Star_Point.value'
        db.alter_column(u'CarSpaApp_reset_star_point', 'value', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Reset_Star_Point.saloon_value'
        db.alter_column(u'CarSpaApp_reset_star_point', 'saloon_value', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'CarSpaApp.car_number': {
            'Meta': {'object_name': 'Car_number'},
            'car_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CarSpaApp.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'CarSpaApp.car_type': {
            'Meta': {'object_name': 'Car_Type'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'CarSpaApp.customer': {
            'Full_Name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'Meta': {'object_name': 'Customer'},
            'customer_ID': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tel_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'CarSpaApp.reset_star_point': {
            'Meta': {'object_name': 'Reset_Star_Point'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saloon_value': ('django.db.models.fields.IntegerField', [], {}),
            'suv_value': ('django.db.models.fields.IntegerField', [], {}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'CarSpaApp.service_category': {
            'Meta': {'object_name': 'Service_Category'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'CarSpaApp.service_rendered': {
            'Meta': {'ordering': "('-category', '-date_created')", 'unique_together': "(('service_Name', 'car_type'),)", 'object_name': 'Service_Rendered'},
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
        u'CarSpaApp.servicetransaction': {
            'Meta': {'object_name': 'ServiceTransaction'},
            'Transxn': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transaction'", 'to': u"orm['CarSpaApp.Transaction']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servcTransID': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'service'", 'to': u"orm['CarSpaApp.Service_Rendered']"}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'worker'", 'to': u"orm['CarSpaApp.Worker']"})
        },
        u'CarSpaApp.star_point': {
            'Meta': {'object_name': 'Star_Point'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CarSpaApp.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'CarSpaApp.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'TransID': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'attendance': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CarSpaApp.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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