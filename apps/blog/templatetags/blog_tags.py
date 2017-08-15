__author__ = 'oldpan'
__date__ = '2017/8/14 10:00'

from django.db.models.aggregates import Count
from ..models import Blog, Category, Tag
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
    return Category.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)
