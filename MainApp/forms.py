from django import forms
from .models import Post, Category
from .models import Debate
# hard-coded version of selection list of categories (not used)
# choices = [('economics', 'economics'), ('philosophy', 'philosophy'), ('medicine', 'medicine'), ('politics', 'politics')]
choices = Category.objects.all().values_list('category', 'category')
choice_list = []
for item in choices:
    choice_list.append(item)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Debate
        fields = ['category', 'title', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'sia', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }