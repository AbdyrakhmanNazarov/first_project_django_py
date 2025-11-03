from django import template

register = template.Library()


@register.filter(name="capital")
def capital(val: str):
    return val.capitalize()
