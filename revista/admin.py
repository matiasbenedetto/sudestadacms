#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from revista.models import *
from adminsortable.admin import SortableAdminMixin
from django.forms import CheckboxSelectMultiple
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage
from suit_redactor.widgets import RedactorWidget


class CustomFlatpageForm(FlatpageForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'es'})
        }


class CustomFlatPageAdmin(FlatPageAdmin):
    form = CustomFlatpageForm


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

	list_display = ('titulo', 'edicion',  'autor', 'publicado', 'visible_en_portada', 'principal', 'permitir_comentarios')
	list_editable = ('publicado', 'visible_en_portada', 'principal', 'permitir_comentarios') 
	search_fields = ('titulo',)
	list_display_links = ('titulo',)
	prepopulated_fields = {'slug': ('titulo',)}
	inlines = [
        ArchivoInline,
    ]


class AutorAdmin(admin.ModelAdmin):
	model=Autor
	list_display = ('nombre', 'sitio')
	search_fields = ('nombre', 'email', 'sitio', 'facebook', 'twitter')
	prepopulated_fields = {'slug': ('nombre',)}


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


class EdicionAdmin (admin.ModelAdmin):
	model=Edicion
	prepopulated_fields = {'slug': ('titulo',)}
	list_display=('titulo', 'coleccion', 'numero', 'especial', 'visible', 'cantidad_de_articulos')
	search_fields = ('titulo',)


class ColeccionAdmin (admin.ModelAdmin):
	model=Coleccion
	prepopulated_fields = {'slug': ('titulo',)}
	list_display=('titulo', 'visible', 'cantidad_de_ediciones')
	search_fields = ('titulo',)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)

admin.site.register(Articulo, ArticuloModelAdmin)
admin.site.register(Edicion, EdicionAdmin)
admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Seccion, SeccionModelAdmin)
admin.site.register(Link, LinkModelAdmin)
admin.site.register(Archivo, ArchivoModelAdmin)