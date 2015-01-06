from django.shortcuts import render, render_to_response
from django.template import RequestContext
from revista.models import *

def index (request):
	ultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[0]
	articulos_ultima_edicion=Articulo.objects.all()
	#anteultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[1]
	ediciones=Edicion.objects.filter(visible=True, especial=False).exclude(numero=None).order_by('numero').reverse()[:4]
	articulos_mas_vistos=Articulo.objects.all().order_by("vistas").reverse()[:10]

	especiales=Edicion.objects.filter(especial=True, visible=True)[:4]
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def articulo(request, id_articulo, slug):
	articulo=Articulo.objects.get(id=id_articulo)
	#articulos_relacionados=Articulo.objects.filter(publicado=True, secciones__in=articulo.secciones)
	edicion=articulo.edicion
	return render_to_response("articulo.html", locals(), context_instance=RequestContext(request))