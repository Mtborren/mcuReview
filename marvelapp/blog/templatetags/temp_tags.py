from django import template

register = template.Library()

from blog.models import Featured, Category, Post



