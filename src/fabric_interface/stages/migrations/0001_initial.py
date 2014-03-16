# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stage'
        db.create_table(u'stages_stage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'], null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=125, null=True, blank=True)),
        ))
        db.send_create_signal(u'stages', ['Stage'])

        # Adding M2M table for field host on 'Stage'
        m2m_table_name = db.shorten_name(u'stages_stage_host')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('stage', models.ForeignKey(orm[u'stages.stage'], null=False)),
            ('host', models.ForeignKey(orm[u'hosts.host'], null=False))
        ))
        db.create_unique(m2m_table_name, ['stage_id', 'host_id'])


    def backwards(self, orm):
        # Deleting model 'Stage'
        db.delete_table(u'stages_stage')

        # Removing M2M table for field host on 'Stage'
        db.delete_table(db.shorten_name(u'stages_stage_host'))


    models = {
        u'hosts.host': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Host'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '175', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'projects.project': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'})
        },
        u'stages.stage': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Stage'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hosts.Host']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']", 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stages']