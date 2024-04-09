from django import template
from base.models import Category

register = template.Library()


@register.inclusion_tag('base/category.html')
def get_category(selected=0):
    category = Category.objects.all()
    return {'category': category, 'selected': selected}
