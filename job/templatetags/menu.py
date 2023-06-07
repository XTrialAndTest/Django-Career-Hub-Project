from django import template
from job.models import Category

register = template.Library()


@register.inclusion_tag("core/menu.html")
def menu():
    category = Category.objects.all()
    return {'category': category}
