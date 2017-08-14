__author__ = 'oldpan'
__date__ = '2017/8/14 16:31'

from django.conf.urls import url
from .views import CommentView


app_name = 'comments'

urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', CommentView.as_view(), name='post_comment'),
]
