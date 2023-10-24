from django import forms
from App_Blog.models import Blog, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ('blog_title', 'blog_content', 'blog_image')

# class UpdateBlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ('blog_title', 'blog_content', 'blog_image')

# class UpdateCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment',)

# class SearchForm(forms.Form):
#     search = forms.CharField(max_length=100)

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

# class ReplyForm(forms.Form):
#     reply = forms.CharField(widget=forms.Textarea)

# class ReplyCommentForm(forms.Form):
#     reply = forms.CharField(widget=forms.Textarea)

# class ReplyReplyForm(forms.Form):
#     reply = forms.CharField(widget=forms.Textarea)

