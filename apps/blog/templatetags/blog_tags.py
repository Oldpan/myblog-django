__author__ = 'oldpan'
__date__ = '2017/8/14 10:00'

from ..models import Blog, Category
from django import template


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Blog.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Blog.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
