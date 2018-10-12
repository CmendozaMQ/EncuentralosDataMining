# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0009_auto_20180126_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapdata',
            name='permalink_url',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_author',
        ),
        migrations.RemoveField(
            model_name='scrapdatamessageblank',
            name='permalink_url',
        ),
        migrations.RemoveField(
            model_name='scrapdatamessageblank',
            name='status_author',
        ),
    ]
