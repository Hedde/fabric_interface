# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=u'created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name=u'modified', editable=False, blank=True)),
                ('project', models.ForeignKey(to='projects.Project', to_field=u'id')),
                ('stage', models.ForeignKey(to_field=u'id', blank=True, to='stages.Stage', null=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=500, null=True, blank=True)),
                ('value_number', models.FloatField(default=0, null=True, verbose_name='Value', blank=True)),
                ('value_boolean', models.BooleanField(default=False, verbose_name='Value')),
                ('data_type', models.CharField(default='STRING', max_length=10, null=True, blank=True, choices=[('BOOLEAN', u'Boolean'), ('NUMBER', u'Number'), ('STRING', u'String')])),
                ('prompt', models.BooleanField(default=False, help_text=u'Prompt me before deploying')),
                ('sensitive_value', models.BooleanField(default=False, help_text=u'Sensitive value that should not be logged')),
            ],
            options={
                u'permissions': (('view_configuration', u'Can view configuration'),),
            },
            bases=(models.Model,),
        ),
    ]
