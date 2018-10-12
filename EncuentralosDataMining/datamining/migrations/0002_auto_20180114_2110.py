# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapdata',
            name='link_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='scrapdata',
            name='permalink_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='scrapdata',
            name='status_author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='scrapdata',
            name='status_link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='scrapdata',
            name='status_message',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='scrapdata',
            name='status_type',
            field=models.CharField(max_length=255),
        ),
    ]
