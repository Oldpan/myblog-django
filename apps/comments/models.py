from django.db import models
from blog.models import Blog


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=u"博客")
    name = models.CharField("称呼", max_length=18)
    email = models.EmailField("邮箱", max_length=50)
    content = models.TextField()
    created_time = models.DateTimeField("发布时间", auto_now_add=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name
