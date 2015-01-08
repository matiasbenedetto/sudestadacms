from django.shortcuts import render, render_to_response
from django.template import RequestContext
from revista.models import *

def index (request):
	ultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[0]
	articulos_ultima_edicion=Articulo.objects.all()
	#anteultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[1]
	ediciones=Edicion.objects.filter(visible=True, especial=False).exclude(numero=None).order_by('numero').reverse()[:4]

	especiales=Edicion.objects.filter(especial=True, visible=True)[:4]
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def articulo(request, id_articulo, slug):
	articulo=Articulo.objects.get(id=id_articulo, slug=slug)
	articulo.vistas=articulo.vistas + 1
	articulo.save()
	
	articulos_relacionados=Articulo.objects.filter(publicado=True)[:4]

	edicion=articulo.edicion
	return render_to_response("articulo.html", locals(), context_instance=RequestContext(request))


def edicion (request, id_edicion, slug):
	edicion=Edicion.objects.get(id=id_edicion, slug=slug)
	return render_to_response("edicion.html", locals(), context_instance=RequestContext(request))
