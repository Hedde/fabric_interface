# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=u'created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name=u'modified', editable=False, blank=True)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
                ('alias', models.CharField(max_length=175)),
                ('slug', models.SlugField(unique=True)),
                ('projects', models.ManyToManyField(to='projects.Project', null=True, verbose_name=u'Projects', blank=True)),
            ],
            options={
                u'ordering': ('-modified', '-created'),
                u'abstract': False,
                u'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
