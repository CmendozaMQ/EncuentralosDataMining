# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0006_scrapdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapdata',
            name='status_id',
            field=models.CharField(max_length=255),
        ),
    ]
