# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0004_articulo_vistas'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicion',
            name='slug',
            field=models.SlugField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seccion',
            name='slug',
            field=models.SlugField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
