# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('archivo', models.FileField(upload_to=b'archivos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publicado', models.BooleanField(default=False)),
                ('visible_en_portada', models.BooleanField(default=False)),
                ('columna', models.IntegerField(blank=True, null=True, choices=[(1, b'Columna 1'), (2, b'Columna 2'), (3, b'Columna 3')])),
                ('fecha', models.DateTimeField()),
                ('volanta', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100, blank=True)),
                ('bajada', models.TextField(blank=True)),
                ('texto', redactor.fields.RedactorField()),
                ('imagen', models.ImageField(default=None, upload_to=b'img-articulos', blank=True)),
                ('video', embed_video.fields.EmbedVideoField(default=None, null=True, blank=True)),
                ('principal', models.BooleanField(default=False)),
                ('edicion_en_papel', models.BooleanField(default=False)),
                ('permitir_comentarios', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('imagen', models.ImageField(default=None, upload_to=b'img-ediciones', blank=True)),
                ('fecha', models.DateTimeField()),
                ('numero', models.IntegerField(null=True, blank=True)),
                ('especial', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('orden',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100, blank=True)),
                ('descripccion', models.TextField(blank=True)),
                ('activa', models.BooleanField(default=True)),
                ('mostrar_en_menu_superior', models.BooleanField(default=True)),
                ('mostrar_en_menu_footer', models.BooleanField(default=True)),
                ('orden', models.PositiveIntegerField(default=0)),
                ('padre', models.ForeignKey(default=None, blank=True, to='revista.Seccion', null=True)),
            ],
            options={
                'ordering': ('orden',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='articulo',
            name='edicion',
            field=models.ForeignKey(default=None, blank=True, to='revista.Edicion', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='secciones',
            field=models.ManyToManyField(default=None, to='revista.Seccion', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archivo',
            name='articulo',
            field=models.ForeignKey(default=None, blank=True, to='revista.Articulo', null=True),
            preserve_default=True,
        ),
    ]
