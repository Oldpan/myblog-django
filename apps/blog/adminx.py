__author__ = 'oldpan'
__date__ = '2017/8/10 19:51'


from .models import Blog, Tag, Category
from comments.models import Comment
import xadmin


class BlogAdmin(object):
    list_display = ['title', 'abstract', 'author',  'content', 'created_time', 'tags', 'category']
    search_fields = ['title', 'author',  'content', 'tags', 'category']
    list_filter = ['title', 'author',  'content', 'created_time', 'tags', 'category']


class TagAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CommentAdmin(object):
    list_display = ['blog', 'name', 'url', 'email', 'content', 'created_time']
    search_fields = ['blog', 'name', 'email', 'content']
    list_filter = ['blog', 'name', 'url', 'email', 'content']


xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Comment, CommentAdmin)
