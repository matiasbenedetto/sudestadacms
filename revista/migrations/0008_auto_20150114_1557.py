# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0007_auto_20150114_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccion',
            name='descripccion',
            field=models.TextField(default=None, blank=True),
            preserve_default=False,
        ),
    ]
