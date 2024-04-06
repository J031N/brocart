from django import template

register=template.Library()

@register.simple_tag(name='multiply')

def multiplication(a,b):
    return a*b