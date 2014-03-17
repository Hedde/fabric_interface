# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]
