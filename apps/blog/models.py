from django.db import models
from datetime import datetime
from django.urls import reverse


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
    abstract = models.CharField(max_length=250, verbose_name=u"摘要")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章信息"
        verbose_name_plural = verbose_name

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:article_page', kwargs={'pk': self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=u"博客")
    name = models.CharField("称呼", max_length=18)
    email = models.EmailField("邮箱", max_length=50)
    content = models.CharField("内容", max_length=300)
    created_time = models.DateTimeField("发布时间", auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name

