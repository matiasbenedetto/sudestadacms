# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from revista.models import *
from forms import *
from sudestada import settings
from django.core.mail import EmailMessage


def index (request):
	ultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[0]
	articulos_ultima_edicion=ultima_edicion.articulo_set.filter(visible_en_portada=True, publicado=True)

	anteultima_edicion=Edicion.objects.filter(visible=True).exclude(numero=None).order_by('numero').reverse()[1]
	articulos_anteultima_edicion=anteultima_edicion.articulo_set.filter(visible_en_portada=True, publicado=True)

	ediciones=Edicion.objects.filter(visible=True, especial=False).exclude(numero=None).order_by('numero').reverse()[:4]

	colecciones_especiales =[]
	for coleccion in Coleccion.objects.filter(especial=True):
		colecciones_especiales.append({
					"coleccion":coleccion,
					"ediciones":coleccion.edicion_set.all().order_by("id").reverse()[:4]
				})			
	return render_to_response("index.html", locals(), context_instance=RequestContext(request))


def busqueda_resultados (request):

	return render_to_response("busqueda_resultados.html", locals(), context_instance=RequestContext(request))


def articulo(request, id_articulo, slug):
	articulo=Articulo.objects.get(id=id_articulo, slug=slug)
	articulo.vistas=articulo.vistas + 1
	articulo.save()
	
	articulos_relacionados=Articulo.objects.filter(publicado=True, edicion=articulo.edicion).exclude(id=articulo.id).order_by("vistas").reverse()[:6]

	edicion=articulo.edicion
	return render_to_response("articulo.html", locals(), context_instance=RequestContext(request))


def articulo_migrar(request):
	id=int(request.GET['id_article'])
	articulo = get_object_or_404(Articulo, id=id)
	return redirect(articulo, permanent=True)


def edicion_migrar(request):
	id=int(request.GET['id_rubrique'])
	edicion = get_object_or_404(Edicion, id=id)
	return redirect(edicion, permanent=True)


def index_migrar(request):
	return redirect("/", permanent=True)


def edicion (request, id_edicion, slug):
	edicion=Edicion.objects.get(id=id_edicion, slug=slug)
	return render_to_response("edicion.html", locals(), context_instance=RequestContext(request))


def coleccion (request, id_coleccion=None, slug=None):
	coleccion=Coleccion.objects.get(id=id_coleccion, slug=slug)
	ediciones=Edicion.objects.filter(coleccion=coleccion).order_by('fecha').reverse()
	return render_to_response("coleccion.html", locals(), context_instance=RequestContext(request))


def comprar (request):
	return redirect("/contacto/")


def seccion (request, slug):
	seccion=get_object_or_404(Seccion, slug=slug)
	articulos_list = seccion.articulo_set.filter(publicado=True)

	paginator = Paginator(articulos_list, 9)
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


def contacto(request):
	form = ContactoForm()
	if request.method == "POST":
		form = ContactoForm(request.POST)
		if  form.is_valid():
			msg = EmailMessage(
	                       'Contacto desde el sitio web',
	                       ('<h1>Contacto desde el sitio web</h1><h2>Nombre: %s</h2>Email: %s <br>Mensaje:%s<br>Telefono:%s<br>Direccion:%s' % (form.cleaned_data["nombre"], form.cleaned_data["email"], form.cleaned_data["texto"], form.cleaned_data["telefono"], form.cleaned_data["direccion"])),
	                       settings.DEFAULT_FROM_EMAIL,
	                       ['sudestadarevista@yahoo.com.ar','matias.benedetto@gmail.com']
			                  )
			msg.content_subtype = "html"
			msg.send()

			msg = EmailMessage(
	                       'Contacto Revista Sudestada',
	                       ('<h1>Gracias por escribirnos.</h1>Ya recibimos tu mensaje, te contestaremos lo más rapido posible. <br><br>Saludos!<br>Revista Sudestada<br>http://revistasudestada.com.ar<br><br><small>Este es un mail automático, no lo respondas.</small>'),
	                       settings.DEFAULT_FROM_EMAIL,
	                       [form.cleaned_data["email"]]
			                  )
			msg.content_subtype = "html"
			msg.send()

	return render_to_response("contacto.html", locals(), context_instance=RequestContext(request))


