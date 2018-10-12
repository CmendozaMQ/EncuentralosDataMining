# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scrapdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField()),
                ('status_message', models.CharField(max_length=200)),
                ('status_author', models.CharField(max_length=200)),
                ('link_name', models.CharField(max_length=250)),
                ('status_type', models.CharField(max_length=250)),
                ('status_link', models.CharField(max_length=250)),
                ('permalink_url', models.CharField(max_length=250)),
                ('status_published', models.DateTimeField()),
                ('status_published_1', models.DateTimeField()),
            ],
        ),
    ]
