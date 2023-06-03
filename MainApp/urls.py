from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#from .views import Home, Philosophy_Blog, ArticleDetailView, AddEntryView, EditPostView, DeletePostView
from .views import post_detail, post_list, debate_list, debate_detail, philosophy_blog, AddBlogView, UpdateBlogView, \
    DeleteBlogView

app_name = 'MainApp'

urlpatterns = [
    #path('', Home.as_view(), name="home"),
    path('', views.post_list, name='post_list'),
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('blog_post/<int:pk>/', post_detail.as_view(), name='post_detail'),
    #path('<int:debate_id>/comment/',views.debate_post, name="debate_post")
    path('debate_list/', debate_list.as_view(), name='debate_list'),
    path('debate/<int:pk>/', debate_detail.as_view(), name='debate-details'),
    path('philosophy/', views.post_list, name='philosophy_blog_list'),
    path('economics/', views.post_list, name='economics_blog_list'),
    path('add_post/', AddBlogView.as_view(), name="add_post"),
    path('blog_post/edit/<int:pk>', UpdateBlogView.as_view(), name='update_post'),
    path('blog_post/delete/<int:pk>', DeleteBlogView.as_view(), name='delete_post'),
]