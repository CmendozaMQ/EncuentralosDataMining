# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0003_remove_scrapdata_status_published_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapdata',
            name='link_name',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='permalink_url',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_author',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_id',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_link',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_message',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_published',
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_type',
        ),
    ]
