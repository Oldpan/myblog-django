__author__ = 'oldpan'
__date__ = '2017/8/11 9:37'


from django.conf.urls import url
from blog.views import BlogView


urlpatterns = [
    url(r'^$', BlogView.as_view(),  name='blog_page'),
]