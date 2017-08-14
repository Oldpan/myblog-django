from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from django.views import View
from .models import Comment
from .forms import CommentForm


class CommentView(View):
    def get(self, request):
        return render(request, 'article_page.html')

    def post(self, request, post_pk):

        post = get_object_or_404(Blog, pk=post_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'article_page.html', context=context)



