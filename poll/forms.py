from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Poll

class DebateForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('category', 'author', 'opponent', 'description', 'title')

        widgets = {
            'category':forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'author':forms.Select(choices=author_list, attrs={'class': 'form-control'}),
            'opponent':forms.Select(choices=author_list, attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
        }