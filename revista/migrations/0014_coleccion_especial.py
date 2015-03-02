# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0013_auto_20150227_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='coleccion',
            name='especial',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
