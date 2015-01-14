# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0009_auto_20150114_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('biografia_corta', models.TextField(blank=True)),
                ('biografia_larga', models.TextField(blank=True)),
                ('sitio', models.URLField(null=True, blank=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('imagen', models.ImageField(default=None, upload_to=b'img-autores', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
