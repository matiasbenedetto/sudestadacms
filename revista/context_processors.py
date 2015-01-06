from models import Seccion, Link, Articulo

def links(request):
	links = Link.objects.filter(activo=True).order_by('orden')
	return {'links': links}

def secciones(request):
	secciones = Seccion.objects.filter(activa=True).order_by('orden')
	return {'secciones': secciones}