# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0003_auto_20150102_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='vistas',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
