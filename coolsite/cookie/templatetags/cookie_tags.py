from django import template
from cookie.models import *

register = template.Library()
@register.simple_tag(name='appealcats')
def get_categories():
    return Category.objects.all()