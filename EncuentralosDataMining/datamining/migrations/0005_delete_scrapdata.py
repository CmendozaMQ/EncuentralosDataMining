# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamining', '0004_auto_20180114_2142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='scrapdata',
        ),
    ]
