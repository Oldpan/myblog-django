__author__ = 'oldpan'
__date__ = '2017/8/15 16:29'

from haystack import indexes
from .models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

