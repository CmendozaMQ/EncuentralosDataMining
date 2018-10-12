# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0011_saveposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapdata',
            name='found_post',
            field=models.BooleanField(default=False),
        ),
    ]
