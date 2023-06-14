from .models import Post, Category, User
from .models import Debate
from django import forms
from MainApp.models import Profile
# hard-coded version of selection list of categories (not used)
# choices = [('economics', 'economics'), ('philosophy', 'philosophy'), ('medicine', 'medicine'), ('politics', 'politics')]
choices = Category.objects.all().values_list('category', 'category')
choice_list = []
for item in choices:
    choice_list.append(item)

authors = Post.objects.all().values_list('author', 'author')
author_list = []
for person in authors:
    author_list.append(person)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Debate
        fields = ['category', 'title', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(choices=author_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }