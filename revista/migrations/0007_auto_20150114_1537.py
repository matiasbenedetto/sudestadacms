# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0006_auto_20150108_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='coleccion',
            name='descripccion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coleccion',
            name='imagen',
            field=models.ImageField(default=None, upload_to=b'img-coleccionmodels.TextField(blank=True)es', blank=True),
            preserve_default=True,
        ),
    ]
