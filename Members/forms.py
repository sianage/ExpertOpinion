from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from MainApp.models import Profile, Category



class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','github_url', 'linkedin_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EditProfileForm(UserChangeForm):
    github_url = forms.CharField(max_length=100)
    class Meta:
        model = Profile
        fields = ('bio', 'github_url', 'linkedin_url', 'field')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
        }