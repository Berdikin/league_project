from django import template
from insurance95.models import *


register = template.Library()


@register.simple_tag()
def get_type_insurance(filter=None):
    if not filter:
        return type_insurance.objects.all()
    else:
        return type_insurance.objects.filter(type_id=filter)


@register.inclusion_tag('insurance95/list_types.html')
def show_types(sort=None, type_selected=0):
    if not sort:
        types = type_insurance.objects.all()
    else:
        types = type_insurance.objects.order_by(sort)

    return {'types': types, 'type_selected': type_selected}
