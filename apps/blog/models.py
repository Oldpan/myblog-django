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

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:article_page', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.abstract:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.abstract = strip_tags(md.convert(self.content))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Blog, self).save(*args, **kwargs)



