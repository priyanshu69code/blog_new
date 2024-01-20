# myblog/templatetags/nav_tags.py
from django import template
from myblog.models import Category

register = template.Library()


@register.inclusion_tag('categories_dropdown.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
