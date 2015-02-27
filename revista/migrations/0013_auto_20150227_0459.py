# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0012_autor_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to=b'banners')),
                ('vinculo', models.CharField(max_length=255, null=True, blank=True)),
                ('orden', models.PositiveIntegerField(default=1)),
                ('mostrar_titulo', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='autor',
            field=models.ManyToManyField(to='revista.Autor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autor',
            name='biografia_larga',
            field=redactor.fields.RedactorField(blank=True),
            preserve_default=True,
        ),
    ]
