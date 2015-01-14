# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0010_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(default=None, to='revista.Autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='slug',
            field=models.SlugField(default=None, max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
