from django.shortcuts import render
from django.views import View
from .models import Blog, Comment, Tag, Category

# Create your views here.


class BlogView(View):
    # 博客预览
    def get(self, request):

        all_articles = Blog.objects.all()

        return render(request, 'blog_page.html', {"all_articles": all_articles})


# 文章内容显示
class ArticleView(View):
    # 文章

    def get(self, request):

        all_articles = Blog.objects.all()
        all_comments = Comment.objects.all()
        all_tags = Tag.objects.all()
        all_category = Category.objects.all()

        return render(request, 'article_page.html', {
            "all_articles": all_articles,
            "all_comments": all_comments,
            "all_tags": all_tags,
            "all_category": all_category
        })



