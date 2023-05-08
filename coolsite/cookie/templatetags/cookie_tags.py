from django import template
from cookie.models import *

register = template.Library()
@register.simple_tag(name='appealcats')
def get_categories(fileter=None):
    if not fileter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=fileter)

@register.inclusion_tag('cookie/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}