from models import Seccion, Link, Articulo

def links(request):
	links = Link.objects.filter(activo=True).order_by('orden')
	return {'links': links}


def secciones(request):
	secciones = Seccion.objects.filter(activa=True).order_by('orden')
	return {'secciones': secciones}


def articulos_mas_vistos(request):
	articulos_mas_vistos = Articulo.objects.filter(publicado=True).order_by("vistas").reverse()[:5]
	return {'articulos_mas_vistos' : articulos_mas_vistos}