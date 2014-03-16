# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Host'
        db.create_table(u'hosts_host', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=175, null=True, blank=True)),
        ))
        db.send_create_signal(u'hosts', ['Host'])


    def backwards(self, orm):
        # Deleting model 'Host'
        db.delete_table(u'hosts_host')


    models = {
        u'hosts.host': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Host'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '175', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        }
    }

    complete_apps = ['hosts']