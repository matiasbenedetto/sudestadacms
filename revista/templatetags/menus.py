from django import template
from revista.models import Menu

register = template.Library()

@register.inclusion_tag('menu.html')
def get_menu(ubicacion=None):
    menu = Menu.objects.get(ubicacion=ubicacion)
    print(menu)
    return {'menu': menu}