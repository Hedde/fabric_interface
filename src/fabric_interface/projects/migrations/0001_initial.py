# encoding: utf8
from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name=u'created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name=u'modified', editable=False, blank=True)),
                ('title', models.CharField(max_length=125)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                u'permissions': (('view_project', u'Can view project'),),
            },
            bases=(models.Model,),
        ),
    ]
