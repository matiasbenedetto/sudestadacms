# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0005_auto_20150108_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('slug', models.SlugField(default=b'', max_length=100)),
                ('visible', models.BooleanField(default=True)),
                ('imagen', models.ImageField(default=None, upload_to=b'img-colecciones', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='edicion',
            name='coleccion',
            field=models.ForeignKey(default=None, blank=True, to='revista.Coleccion', null=True),
            preserve_default=True,
        ),
    ]
