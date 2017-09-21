from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.html import strip_tags
import markdown


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"分类名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"标签名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=32, verbose_name=u"文章标题")
    author = models.CharField(max_length=18, verbose_name=u"作者")
    content = models.TextField(verbose_name=u'博客正文')
    created_time = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(Category, verbose_name=u"分类")
    tags = models.ManyToManyField(Tag, verbose_name=u"标签")
    abstract = models.CharField(max_length=250, verbose_name=u"摘要", blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章信息"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:article_page', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):

        if not self.abstract:

            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])

            self.abstract = strip_tags(md.convert(self.content))[:250]

        super(Blog, self).save(*args, **kwargs)



