# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0010_auto_20180207_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='savePosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.CharField(max_length=255)),
                ('status_message', models.CharField(max_length=255)),
                ('link_name', models.CharField(max_length=255)),
                ('status_type', models.CharField(max_length=255)),
                ('status_link', models.CharField(max_length=255)),
                ('status_published', models.DateTimeField()),
            ],
        ),
    ]
