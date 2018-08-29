# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0015_menu_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
