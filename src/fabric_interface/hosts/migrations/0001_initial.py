# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=u'created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name=u'modified', editable=False, blank=True)),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('alias', models.CharField(max_length=175, null=True, blank=True)),
            ],
            options={
                u'ordering': ('-modified', '-created'),
                u'abstract': False,
                u'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
