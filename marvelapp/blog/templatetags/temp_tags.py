from django import template

register = template.Library()

from blog.models import Featured, Category, Post


@register.simple_tag
def heroes():
    feat_menu = Featured.objects.all()
    context = {
        'feat_menu': feat_menu
    }
    return context