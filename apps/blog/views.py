from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Blog, Comment, Tag, Category

# Create your views here.


class BlogView(View):
    # 博客预览
    def get(self, request):

        post_list = Blog.objects.all().order_by('-created_time')

        return render(request, 'blog_page.html', {"post_list": post_list})


# 文章内容显示
class ArticleView(View):
    # 文章

    def get(self, request, pk):

        post = get_object_or_404(Blog, pk=pk)

        return render(request, 'article_page.html', context={'post': post})



