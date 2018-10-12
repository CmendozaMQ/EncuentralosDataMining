# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0008_scrapdata_status_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='scrapdataMessageBlank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.CharField(max_length=255)),
                ('status_message', models.CharField(max_length=255)),
                ('status_author', models.CharField(max_length=255)),
                ('link_name', models.CharField(max_length=255)),
                ('status_type', models.CharField(max_length=255)),
                ('status_link', models.CharField(max_length=255)),
                ('permalink_url', models.CharField(max_length=255)),
                ('status_published', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='scrapdata',
            name='status_post',
        ),
    ]
