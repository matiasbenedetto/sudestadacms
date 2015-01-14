# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0008_auto_20150114_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccion',
            name='imagen',
            field=models.ImageField(default=None, upload_to=b'img-colecciones', blank=True),
            preserve_default=True,
        ),
    ]
