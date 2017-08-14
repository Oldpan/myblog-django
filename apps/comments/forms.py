__author__ = 'oldpan'
__date__ = '2017/8/14 16:13'


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'content']
