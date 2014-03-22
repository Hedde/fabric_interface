# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=u'created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name=u'modified', editable=False, blank=True)),
                ('project', models.ForeignKey(to_field=u'id', blank=True, to='projects.Project', null=True)),
                ('role', models.CharField(max_length=125, null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('hosts', models.ManyToManyField(to='hosts.Host', null=True, verbose_name=u'Hosts', blank=True)),
            ],
            options={
                u'unique_together': set([('project', 'slug')]),
            },
            bases=(models.Model,),
        ),
    ]
