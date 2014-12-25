#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from revista.models import *
from adminsortable.admin import SortableAdminMixin
from django.forms import CheckboxSelectMultiple



class ArchivoInline(admin.TabularInline):
    model = Archivo


class ArchivoModelAdmin(admin.ModelAdmin):
	model = Archivo
	list_display = ('titulo', 'archivo')


class ArticuloModelAdmin(admin.ModelAdmin):
	model = Articulo
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple()},
    }
	#filter_horizontal =("secciones",)

	list_display = ('columna', 'titulo', 'publicado', 'visible_en_portada', 'principal', 'edicion_en_papel', 'permitir_comentarios')
	list_editable = ('columna', 'publicado', 'visible_en_portada', 'principal', 'edicion_en_papel', 'permitir_comentarios') 
	search_fields = ('titulo',)
	list_display_links = ('titulo',)
	prepopulated_fields = {'slug': ('titulo',)}
	inlines = [
        ArchivoInline,
    ]


class LinkModelAdmin(SortableAdminMixin, admin.ModelAdmin):
	model = Link
	list_display = ('titulo', 'url', 'activo',)
	list_editable = ('activo',) 
	search_fields = ('titulo',)
	list_display_links = ('titulo', 'url')


class SeccionModelAdmin(SortableAdminMixin, admin.ModelAdmin):
	model = Seccion
	list_display = ('titulo', 'activa', 'mostrar_en_menu_superior', 'mostrar_en_menu_footer')
	list_editable = ('activa', 'mostrar_en_menu_superior', 'mostrar_en_menu_footer') 
	search_fields = ('titulo',)
	list_display_links = ('titulo',)
	prepopulated_fields = {'slug': ('titulo',)}
	radio_fields = {"padre": admin.HORIZONTAL}


admin.site.register(Articulo, ArticuloModelAdmin)
admin.site.register(Seccion, SeccionModelAdmin)
admin.site.register(Link, LinkModelAdmin)
admin.site.register(Archivo, ArchivoModelAdmin)