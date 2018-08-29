#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from redactor.fields import RedactorField
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import get_thumbnail


class Menu (models.Model):

    def __unicode__(self):
        return unicode(self.titulo) or u''

    titulo=models.CharField(max_length=255)
    ubicacion=models.CharField(max_length=255, unique=True)


class MenuItem (models.Model):

    def __unicode__(self):
        return unicode(self.titulo) or u''

    titulo=models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu)


class Seccion (models.Model):
    
    def __unicode__(self):
        return unicode(self.titulo) or u''
    
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


class Autor (models.Model):

    def __unicode__(self):
        return unicode(self.nombre) or u''

    nombre = models.CharField(max_length=255)
    slug =  models.SlugField(blank=True, max_length=100)
    biografia_corta = models.TextField(blank=True)
    biografia_larga = RedactorField(blank=True)
    email = models.EmailField(blank=True, null=True)
    sitio = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='img-autores', blank=True, default=None)

    def thumb(self):
        if self.imagen:
            img = get_thumbnail(self.imagen, '80x80', crop='center', quality=99)
            return '<img src="%s" width="80" height="80" />' % (img.url)
        else:
            return None
    thumb.allow_tags = True


class Coleccion (models.Model):

    def __unicode__(self):
        return unicode(self.titulo) or u''

    titulo=models.CharField(max_length=255, blank=True, null=True, default=None)
    slug =  models.SlugField(max_length=100, default="")
    visible=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to='img-colecciones', blank=True, default=None)
    descripccion=models.TextField(blank=True)
    especial=models.BooleanField(default=True)

    def ediciones (self):
        return Edicion.objects.filter(coleccion=self, visible=True)

    def cantidad_de_ediciones (self):
        return Edicion.objects.filter(coleccion=self, visible=True).count()

    def get_absolute_url(self):
        return "/coleccion/%i/%s/" % (self.id, self.slug) 


class Edicion (models.Model):

    def __unicode__(self):
        return unicode(self.titulo) or u''

    titulo=models.CharField(max_length=255, blank=True, null=True, default=None)
    slug =  models.SlugField(max_length=100, default="")
    imagen=models.ImageField(upload_to='img-ediciones', blank=True, default=None)
    fecha=models.DateTimeField()
    numero=models.IntegerField(blank=True, null=True)
    especial=models.BooleanField(default=False)
    visible=models.BooleanField(default=True)
    coleccion=models.ForeignKey(Coleccion, default=None, blank=True, null=True)

    def articulos (self):
        return Articulo.objects.filter(edicion=self, publicado=True).order_by("orden")

    def cantidad_de_articulos (self):
        return Articulo.objects.filter(edicion=self, publicado=True).count()

    def thumb(self):
        if self.imagen:
            img = get_thumbnail(self.imagen, '90x120', crop='center', quality=99)
            return '<img src="%s" width="90" height="120" />' % (img.url)
        else:
            return None
    thumb.allow_tags = True

    def get_absolute_url(self):
        return "/edicion/%i/%s/" % (self.id, self.slug) 


class Articulo (models.Model):
    def __unicode__(self):
        return unicode(self.titulo) or u''


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
    autor=models.ManyToManyField(Autor)

    def thumb(self):
        if self.imagen:
            img = get_thumbnail(self.imagen, '150x100', crop='center', quality=99)
            return '<img src="%s" width="100" height="100" />' % (img.url)
        else:
            return None
    thumb.allow_tags = True

    def get_absolute_url(self):
        return "/articulo/%i/%s/" % (self.id, self.slug) 


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


class Banner (models.Model):

    def __unicode__(self):
        return self.titulo

    titulo=models.CharField(max_length=255)
    imagen=models.ImageField(upload_to='banners')
    vinculo=models.CharField(max_length=255, blank=True, null=True)
    orden = models.PositiveIntegerField(default=1)
    mostrar_titulo=models.BooleanField(default=False)
    visible=models.BooleanField(default=True)

    def thumb(self):
        if self.imagen:
            img = get_thumbnail(self.imagen, '150x100', crop='center', quality=99)
            return '<img src="%s" width="100" height="100" />' % (img.url)
        else:
            return None
    thumb.allow_tags = True

