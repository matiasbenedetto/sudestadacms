from models import Seccion, Link, Articulo, Banner

def links(request):
	links = Link.objects.filter(activo=True).order_by('orden')
	return {'links': links}


def secciones(request):
	secciones = Seccion.objects.filter(activa=True).order_by('orden')
	return {'secciones': secciones}


def articulos_mas_vistos(request):
	articulos_mas_vistos = Articulo.objects.filter(publicado=True).order_by("vistas").reverse()[:5]
	return {'articulos_mas_vistos' : articulos_mas_vistos}


def banners(request):
	banners = Banner.objects.filter(visible=True).order_by('orden')
	return {'banners':banners}