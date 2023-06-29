from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from MainApp.forms import NoteForm
from MainApp.models import Profile, Note, Post
from django import forms
from MainApp.models import Profile
from .forms import SignUpForm, ProfilePageForm

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'github_url', 'linkedin_url']
    success_url = reverse_lazy('MainApp:home')


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_profile.html"
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

'''class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')'''

def UserRegisterView(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('MainApp:home')
    return render(request, 'registration/register.html', {'form':form})

class UserEditView(generic.UpdateView):
    form_class = SignUpForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('MainApp:home')

    def get_object(self):
        return self.request.user

'''class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def post(self, request, pk):
        print("pk =",pk)
        if request.user.is_authenticated:
            profile = Profile.objects.get(user_id=pk)

            if request.method == "post":
                current_user_profile = request.user.profile
                action = request.POST['follow']

                if action == 'unfollow':
                    current_user_profile.follows.remove(profile)
                else:
                    current_user_profile.follows.add(profile)
                current_user_profile.save()

            return render(request, 'registration/user_profile.html', {'profile': profile})
        else:
            return redirect('MainApp:home')
    login_url = 'MainApp:home' 
    
    def get(self, request, pk):
        profile = Profile.objects.get(user_id=pk)
        return render(request, 'registration/user_profile.html', {'profile': profile})

    def post(self, request, pk):
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST.get('follow')

            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return redirect('ProfileView', pk=pk)

    def get_context_data(self, *args, **kwargs):
        cat_menu = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context'''

def ProfileView(request, pk):
    '''profile = get_object_or_404(Profile, id=pk)
    cat_menu = Profile.objects.all()

    context = {
        'profile': profile,
        'cat_menu': cat_menu,
        'page_user': profile
    }'''


    if request.user.is_authenticated:
        form = NoteForm(request.POST or None)
        profile = Profile.objects.get(id=pk)
        followed_profiles = request.user.profile.follows.all()
        note = Note.objects.filter(profile__in=followed_profiles)
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']

            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return render(request, 'registration/user_profile.html', {'profile':profile, 'note':note, 'form':form})
    else:
        return redirect('MainApp:home')

    requested_url = request.path
    if request.user.is_authenticated:
        form = NoteForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                note = form.save(commit=False)
                note.profile = request.user.profile
                note.user = request.user
                note.save()
                return redirect('MainApp:home')


        followed_profiles = request.user.profile.follows.all()
        print("FOLLOWING: ",followed_profiles)
        current_user = request.user
        print("URL is......",requested_url)
        home = Post.published.all()
        notes = Note.objects.filter(profile__in=followed_profiles)
        #notes = Note.objects.all().order_by("-created_at")
        paginator = Paginator(home,2)
        page_number = request.GET.get('page', 1)
        #notes = Note.objects.all()
        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            # if page_number not an int, display first page
            posts = paginator.page(1)
        except EmptyPage:
            #If page_number out of range, display last page of results
            posts = paginator.page(paginator.num_pages)
        if requested_url == "/MainApp/philosophy/":
            return render(request, 'MainApp/post/philosophy_blog.html', {'posts': posts})
        elif requested_url == "/MainApp/economics/":
            return render(request, 'MainApp/post/economics.html', {'posts': posts})
        else:
            return render(request, 'MainApp/post/list.html', {'notes': notes, "form":form})
    else:
        return render(request, 'MainApp/post/list.html')
