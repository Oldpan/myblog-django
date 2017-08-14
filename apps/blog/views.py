from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Blog, Tag, Category
from comments.forms import CommentForm
import markdown

# Create your views here.


class BlogView(View):
    # 博客预览
    def get(self, request):

        post_list = Blog.objects.all().order_by('-created_time')

        return render(request, 'blog_page.html', {"post_list": post_list})

# 另外的VIEW函数方法
# from django.views.generic import ListView
#
# class IndexView(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'


# 文章内容显示
class ArticleView(View):
    # 文章

    def get(self, request, pk):

        post = get_object_or_404(Blog, pk=pk)
        post.content = markdown.markdown(post.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])

        post.increase_views()
        form = CommentForm()
        comment_list = post.comment_set.all()

        context = {'post': post,
                   'form': form,
                   'comment_list': comment_list
                   }

        return render(request, 'article_page.html', context=context)


# from django.views.generic import ListView, DetailView
#
# # 记得在顶部导入 DetailView
# class PostDetailView(DetailView):
#     # 这些属性的含义和 ListView 是一样的
#     model = Post
#     template_name = 'blog/detail.html'
#     context_object_name = 'post'
#
#     def get(self, request, *args, **kwargs):
#         # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
#         # get 方法返回的是一个 HttpResponse 实例
#         # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
#         # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
#         response = super(PostDetailView, self).get(request, *args, **kwargs)
#
#         # 将文章阅读量 +1
#         # 注意 self.object 的值就是被访问的文章 post
#         self.object.increase_views()
#
#         # 视图必须返回一个 HttpResponse 对象
#         return response
#
#     def get_object(self, queryset=None):
#         # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
#         post = super(PostDetailView, self).get_object(queryset=None)
#         post.body = markdown.markdown(post.body,
#                                       extensions=[
#                                           'markdown.extensions.extra',
#                                           'markdown.extensions.codehilite',
#                                           'markdown.extensions.toc',
#                                       ])
#         return post
#
#     def get_context_data(self, **kwargs):
#         # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
#         # 还要把评论表单、post 下的评论列表传递给模板。
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         form = CommentForm()
#         comment_list = self.object.comment_set.all()
#         context.update({
#             'form': form,
#             'comment_list': comment_list
#         })
#         return context


class ArchivesView(View):

    def get(self, request, year, month):
        post_list = Blog.objects.filter(created_time__year=year,
                                        created_time__month=month
                                        ).order_by('-created_time')
        return render(request, 'blog_page.html', {'post_list': post_list})


class CategoryView(View):

    def get(self, request, pk):
        cate = get_object_or_404(Category, pk=pk)
        post_list = Blog.objects.filter(category=cate).order_by('-created_time')
        return render(request, 'blog_page.html', {'post_list': post_list})


# 另外的Category_view方法
# class CategoryView(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
#         return super(CategoryView, self).get_queryset().filter(category=cate)
