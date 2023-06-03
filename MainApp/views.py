from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from MainApp.models import Post, Category, Profile
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, CreateView
from .models import Post, Debate, Category, Comment, User
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
#from .forms import PostForm
'''class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']'''

def post_list(request):
    requested_url = request.path
    print("URL is......",requested_url)
    post_list = Post.published.all()
    paginator = Paginator(post_list,10)
    page_number = request.GET.get('page', 1)
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
        return render(request, 'MainApp/post/list.html', {'posts': posts})

class post_detail(DetailView, ):
    model = Post
    template_name = 'MainApp/post/detail.html'
    success_url = reverse_lazy('post_detail')

@require_POST
def debate_post(request, debate_id):
    post = get_object_or_404(Debate, id=debate_id)
    comment = None
    #???????????????????????????????
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'MainApp/debate/comment.html',
                  {'post':post, 'form':form, 'comment':comment})

class debate_list(ListView):
    model = Debate
    template_name = 'MainApp/debate/debate_list.html'

class debate_detail(DetailView):
    model = Debate
    template_name = 'MainApp/debate/debate_detail.html'

class philosophy_blog(ListView):
    model = Post
    template_name = 'MainApp/post/philosophy_blog.html'

class AddBlogView(CreateView):
    model = Post
    #form_class = PostForm
    template_name = 'MainApp/post/add_post.html'
    fields = '__all__'
    #success_url = reverse_lazy('MainApp:philosophy_blog_list')
    success_url = reverse_lazy('MainApp/post/list.html')

class UpdateBlogView(UpdateView):
    model = Post
    template_name = 'MainApp/post/update_blog.html'
    fields = ['title', 'body']

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'MainApp/post/delete_blog.html'
    success_url = reverse_lazy('MainApp:philosophy_blog_list')

