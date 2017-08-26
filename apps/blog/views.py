from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.views.generic import ListView, DetailView
from .models import Blog, Tag, Category
from comments.forms import CommentForm
import markdown


# Create your views here.


class BlogView(ListView):
    model = Blog
    template_name = 'blog_page.html'
    context_object_name = 'post_list'

    paginate_by = 3

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)

        context.update(pagination_data)

        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:

            return {}

        left = []

        right = []

        left_has_more = False

        right_has_more = False

        first = False

        last = False

        page_number = page.number

        total_pages = paginator.num_pages

        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 2]

            if right[-1] < total_pages - 1:
                right_has_more = True

            if right[-1] < total_pages:
                last = True

        elif page_number == total_pages:

            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

            if left[0] > 2:
                left_has_more = True

            if left[0] > 1:
                first = True
        else:

            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]

            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data


# class BlogView(View):
#     # 博客预览
#     def get(self, request):
#
#         post_list = Blog.objects.all().order_by('-created_time')
#
#         return render(request, 'blog_page.html', {"post_list": post_list})

# 另外的VIEW函数方法
# from django.views.generic import ListView
#
# class IndexView(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'


# # 文章内容显示
# class ArticleView(View):
#     # 文章
#
#     def get(self, request, pk):
#         post = get_object_or_404(Blog, pk=pk)
#         post.content = markdown.markdown(post.content, extensions=[
#             'markdown.extensions.extra',
#             'markdown.extensions.codehilite',
#             'markdown.extensions.toc',
#         ])
#
#         post.increase_views()
#         form = CommentForm()
#         comment_list = post.comment_set.all()
#
#         context = {'post': post,
#                    'form': form,
#                    'comment_list': comment_list
#                    }
#
#         return render(request, 'article_page.html', context=context)


class ArticleView(DetailView):

    model = Blog
    template_name = 'article_page.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):

        response = super(ArticleView, self).get(request, *args, **kwargs)

        self.object.increase_views()

        return response

    def get_object(self, queryset=None):

        post = super(ArticleView, self).get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        post.content = md.convert(post.content)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):

        context = super(ArticleView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


class ArchivesView(ListView):
    model = Blog
    template_name = 'blog_page.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(
            created_time__year=year,
            created_time__month=month
        ).order_by('-created_time')


# class ArchivesView(View):
#
#     def get(self, request, year, month):
#         post_list = Blog.objects.filter(created_time__year=year,
#                                         created_time__month=month
#                                         ).order_by('-created_time')
#         return render(request, 'blog_page.html', {'post_list': post_list})


# class CategoryView(View):
#
#     def get(self, request, pk):
#         cate = get_object_or_404(Category, pk=pk)
#         post_list = Blog.objects.filter(category=cate).order_by('-created_time')
#         return render(request, 'blog_page.html', {'post_list': post_list})


class CategoryView(ListView):
    model = Blog
    template_name = 'blog_page.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class TagView(ListView):
    model = Blog
    template_name = 'blog_page.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)
