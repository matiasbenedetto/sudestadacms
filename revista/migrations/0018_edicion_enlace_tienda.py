# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0017_auto_20180829_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicion',
            name='enlace_tienda',
            field=models.URLField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
