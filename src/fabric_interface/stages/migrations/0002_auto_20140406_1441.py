# encoding: utf8
from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, blank=True),
        ),
    ]
