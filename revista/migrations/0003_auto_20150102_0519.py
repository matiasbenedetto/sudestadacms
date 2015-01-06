# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0002_articulo_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='columna',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='edicion_en_papel',
        ),
    ]
