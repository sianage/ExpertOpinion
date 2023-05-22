from django import forms
from .models import Post
from .models import Debate
# hard-coded version of selection list of categories (not used)
# choices = [('economics', 'economics'), ('philosophy', 'philosophy'), ('medicine', 'medicine'), ('politics', 'politics')]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Debate
        fields = ['category', 'title', 'description']
