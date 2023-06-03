from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from MainApp.models import Profile


from MainApp.models import Profile
from .forms import SignUpForm
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user

class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context