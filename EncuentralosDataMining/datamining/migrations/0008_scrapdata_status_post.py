# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0007_auto_20180115_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapdata',
            name='status_post',
            field=models.BooleanField(default=False),
        ),
    ]
