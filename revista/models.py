#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from redactor.fields import RedactorField
from embed_video.fields import EmbedVideoField


class Seccion (models.Model):
    def __unicode__(self):
        return self.titulo
    
    titulo=models.CharField(max_length=255)
    slug =  models.SlugField(blank=True, max_length=100)
    descripccion=models.TextField(blank=True)
    activa=models.BooleanField(default=True)
    mostrar_en_menu_superior=models.BooleanField(default=True)
    mostrar_en_menu_footer=models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0, blank=False, null=False)
    padre = models.ForeignKey("self", default=None, blank=True, null=True)
    
    class Meta(object):
        ordering = ('orden',)

    @property
    def hijas(self):
        return Seccion.objects.filter(padre=self.id)


class Articulo (models.Model):
    def __unicode__(self):
        return self.titulo

    COLUMNAS = (
        (1, 'Columna 1'),
        (2, 'Columna 2'),
        (3, 'Columna 3'),
    )

    publicado=models.BooleanField(default=False)
    visible_en_portada=models.BooleanField(default=False)
    columna=models.IntegerField(choices=COLUMNAS, blank=True, null=True)
    fecha=models.DateTimeField()
    volanta=models.CharField(max_length=255, blank=True, null=True, default=None)
    titulo=models.CharField(max_length=255)
    slug =  models.SlugField(blank=True, max_length=100)
    bajada=models.TextField(blank=True)
    texto=RedactorField()
    secciones=models.ManyToManyField(Seccion, blank=True, null=True, default=None)
    imagen=models.ImageField(upload_to='imagenes', blank=True, default=None)
    video = EmbedVideoField(blank=True, null=True, default=None)
    principal=models.BooleanField(default=False)
    edicion_en_papel=models.BooleanField(default=False)
    permitir_comentarios=models.BooleanField(default=True)


class Link (models.Model):
    def __unicode__(self):
        return self.titulo

    titulo=models.CharField(max_length=255)
    url=models.URLField()
    activo=models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('orden',)


class Archivo (models.Model):
    def __unicode__(self):
        return self.titulo

    titulo=models.CharField(max_length=255)
    archivo=models.FileField(upload_to='archivos')
    articulo=models.ForeignKey(Articulo, null=True, blank=True, default=None)
