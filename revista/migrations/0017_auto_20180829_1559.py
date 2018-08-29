# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0016_auto_20180829_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='ubicacion',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
