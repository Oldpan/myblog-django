__author__ = 'oldpan'
__date__ = '2017/8/11 9:37'


from django.conf.urls import url
from blog.views import BlogView, ArticleView, ArchivesView, CategoryView

app_name = 'blog'

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog_page'),
    url(r'^post/(?P<pk>[0-9]+)/$', ArticleView.as_view(), name='article_page'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives_page'),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryView.as_view(), name='category_page'),
]