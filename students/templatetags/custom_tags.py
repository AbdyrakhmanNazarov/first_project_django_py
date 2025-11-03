from django import template
from students.models import Group

register = template.Library()

@register.simple_tag()
def get_groups():
    return Group.objects.all()