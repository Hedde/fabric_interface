# encoding: utf8
from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (u'contenttypes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'date created', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name=u'password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=u'email address', db_index=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=u'Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name=u'Admin')),
                ('first_name', models.CharField(max_length=125, verbose_name=u'First name')),
                ('family_name_prefix', models.CharField(max_length=125, null=True, verbose_name=u'Family name prefix', blank=True)),
                ('family_name', models.CharField(max_length=125, verbose_name=u'Family name')),
                ('content_type', models.ForeignKey(to_field=u'id', editable=False, to=u'contenttypes.ContentType', null=True)),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
