from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from revista.models import *


def index (request):
	ultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[0]
	articulos_ultima_edicion=ultima_edicion.articulo_set.filter(visible_en_portada=True, publicado=True)

	anteultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[1]
	articulos_anteultima_edicion=anteultima_edicion.articulo_set.filter(visible_en_portada=True, publicado=True)

	ediciones=Edicion.objects.filter(visible=True, especial=False).exclude(numero=None).order_by('numero').reverse()[:4]

	especiales=Edicion.objects.filter(especial=True, visible=True).order_by("fecha").reverse()[:4]
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))


def articulo(request, id_articulo, slug):
	articulo=Articulo.objects.get(id=id_articulo, slug=slug)
	articulo.vistas=articulo.vistas + 1
	articulo.save()
	
	articulos_relacionados=Articulo.objects.filter(publicado=True)[:4]

	edicion=articulo.edicion
	return render_to_response("articulo.html", locals(), context_instance=RequestContext(request))


def articulo_migrar(request):
	id=int(request.GET['id_article'])
	articulo = get_object_or_404(Articulo, id=id)
	return redirect(articulo)


def edicion_migrar(request):
	id=int(request.GET['id_rubrique'])
	edicion = get_object_or_404(Edicion, id=id)
	return redirect(edicion)


def edicion (request, id_edicion, slug):
	edicion=Edicion.objects.get(id=id_edicion, slug=slug)
	return render_to_response("edicion.html", locals(), context_instance=RequestContext(request))


def coleccion (request, id_coleccion=None, slug=None):
	coleccion=Coleccion.objects.get(id=id_coleccion, slug=slug)
	ediciones=Edicion.objects.filter(coleccion=coleccion).order_by('fecha').reverse()
	return render_to_response("coleccion.html", locals(), context_instance=RequestContext(request))


def comprar (request):

	return render_to_response("comprar.html", locals(), context_instance=RequestContext(request))


def seccion (request, slug):
	seccion=get_object_or_404(Seccion, slug=slug)
	articulos_list = seccion.articulo_set.filter(publicado=True)

	paginator = Paginator(articulos_list, 3)
	page = request.GET.get('pagina')
	try:
		articulos = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		articulos = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		articulos = paginator.page(paginator.num_pages)

	return render_to_response("seccion.html", locals(), context_instance=RequestContext(request))

