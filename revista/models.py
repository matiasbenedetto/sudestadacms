#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from redactor.fields import RedactorField
from embed_video.fields import EmbedVideoField


class Seccion (models.Model):
    def __unicode__(self):
        return self.titulo
    
    titulo=models.CharField(max_length=255)
    slug =  models.SlugField(max_length=100, default="")
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


class Edicion (models.Model):
    titulo=models.CharField(max_length=255, blank=True, null=True, default=None)
    slug =  models.SlugField(max_length=100, default="")
    imagen=models.ImageField(upload_to='img-ediciones', blank=True, default=None)
    fecha=models.DateTimeField()
    numero=models.IntegerField(blank=True, null=True)
    especial=models.BooleanField(default=False)
    visible=models.BooleanField(default=True)

    def articulos (self):
        return Articulo.objects.filter(edicion=self).order_by("orden")


class Articulo (models.Model):
    def __unicode__(self):
        return self.titulo

    publicado=models.BooleanField(default=False)
    visible_en_portada=models.BooleanField(default=False)
    fecha=models.DateTimeField()
    volanta=models.CharField(max_length=255, blank=True, null=True, default=None)
    titulo=models.CharField(max_length=255)
    slug =  models.SlugField(blank=True, max_length=100)
    bajada=models.TextField(blank=True)
    texto=RedactorField()
    secciones=models.ManyToManyField(Seccion, blank=True, null=True, default=None)
    imagen=models.ImageField(upload_to='img-articulos', blank=True, default=None)
    video = EmbedVideoField(blank=True, null=True, default=None)
    principal=models.BooleanField(default=False)
    edicion=models.ForeignKey(Edicion, default=None, blank=True, null=True)
    permitir_comentarios=models.BooleanField(default=True)
    orden=models.IntegerField(blank=True, null=True)
    vistas=models.IntegerField(default=0)


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
