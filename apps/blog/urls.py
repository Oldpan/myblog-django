__author__ = 'oldpan'
__date__ = '2017/8/11 9:37'


from django.conf.urls import url
from blog.views import BlogView, ArticleView

app_name = 'blog'

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog_page'),
    url(r'^post/(?P<pk>[0-9]+)/$', ArticleView.as_view(), name='article_page'),
]